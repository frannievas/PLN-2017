from math import log2
from collections import defaultdict


class HMM:

    def __init__(self, n, tagset, trans, out):
        """
        n -- n-gram size.
        tagset -- set of tags.
        trans -- transition probabilities dictionary.
        out -- output probabilities dictionary.
        """
        self.start_tag = ["<s>"]
        self.end_tag = ["</s>"]
        self.n = n
        self.tagset = tagset
        self.trans = trans
        self.out = out

    def tagset(self):
        """Returns the set of tags.
        """
        return self.tagset

    def trans_prob(self, tag, prev_tags):
        """Probability of a tag.

        tag -- the tag.
        prev_tags -- tuple with the previous n-1 tags (optional only if n = 1).
        """
        prob = 0.0

        # No tags, empty tuple.
        if self.n == 1:
            prev_tags = ()

        if prev_tags in self.trans and tag in self.trans[prev_tags]:
            prob = self.trans[prev_tags][tag]

        return prob

    def out_prob(self, word, tag):
        """Probability of a word given a tag.

        word -- the word.
        tag -- the tag.
        """
        prob = 0.0

        if tag in self.out and word in self.out[tag]:
            prob = self.out[tag][word]

        return prob

    def tag_prob(self, y):
        """
        Probability of a tagging.
        Warning: subject to underflow problems.

        y -- tagging.
        """
        # TODO: Dado una secuencia de taggs devuelve su probabilidad

        prob = 1.0
        n = self.n
        prev_tags = tuple(self.start_tag*(n-1))
        y_extended = y + self.end_tag

        for tag in y_extended:
            prob *= self.trans_prob(tag, prev_tags)

            # Delete 1 prev_tags and add the "tagg"
            if self.n > 1:
                prev_tags = prev_tags[1:] + (tag,)

        return prob

    def prob(self, x, y):
        """
        Joint probability of a sentence and its tagging.
        Warning: subject to underflow problems.

        x -- sentence.
        y -- tagging.
        """

        prob = 1.0
        tagging_prob = self.tag_prob(y)

        if tagging_prob > 0:
            for i in range(len(x)):
                prob *= self.out_prob(x[i], y[i])

        return tagging_prob * prob

    def tag_log_prob(self, y):
        """
        Log-probability of a tagging.

        y -- tagging.
        """
        log_prob = 0.0
        n = self.n
        prev_tags = tuple(self.start_tag*(n-1))
        y_extended = y + self.end_tag

        for tag in y_extended:
            prob = self.trans_prob(tag, prev_tags)

            # Delete 1 prev_tags and add the "tagg"
            if self.n > 1:
                prev_tags = prev_tags[1:] + (tag,)

            if prob > 0:
                log_prob += log2(prob)
            else:
                log_prob = float("-inf")
                break

        return log_prob

    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.

        x -- sentence.
        y -- tagging.
        """
        log_prob = 0.0
        tagging_prob = self.tag_log_prob(y)

        if tagging_prob != float("-inf"):
            for i in range(len(x)):
                prob = self.out_prob(x[i], y[i])
                if prob > 0:
                    log_prob += log2(prob)
                else:
                    log_prob = float("-inf")
                    break

        # Log(x * y) = log(x) + log(y)
        return tagging_prob + log_prob

    def tag(self, sent):
        """Returns the most probable tagging for a sentence.

        sent -- the sentence.
        """
        return ViterbiTagger(self).tag(sent)


class ViterbiTagger:

    def __init__(self, hmm):
        """
        hmm -- the HMM.
        """
        self.hmm = hmm
        self._pi = {}

    def tag(self, sent):
        """Returns the most probable tagging for a sentence.

        sent -- the sentence.
        """
        hmm = self.hmm
        n = self.hmm.n
        self._pi = pi = {}
        pi[0] = {tuple((n-1) * self.hmm.start_tag): (log2(1.0), [])}
        m = len(sent)

        for k in range(1, m+1):
            pi[k] = {}

            for tag in hmm.tagset:
                # e(Xk|v)
                e = hmm.out_prob(sent[k-1], tag)
                if e > 0:
                    for key in pi[k-1].keys():
                        # q(v | w, t2...tn-1)
                        q = hmm.trans_prob(tag, key)
                        if q > 0:
                            (p, tag_sent) = pi[k-1][key]
                            new_prev = (key + (tag,))[1:]
                            new_prob = p + log2(q) + log2(e)
                            # MAX
                            if (new_prev not in pi[k] or
                                    new_prob > pi[k][new_prev][0]):
                                pi[k][new_prev] = (new_prob, tag_sent + [tag])

        # STOP
        max_prob = float("-inf")
        for key in pi[m].keys():
            prob = hmm.trans_prob('</s>', key)
            if prob > 0.0:
                (p, tag_sent) = pi[m][key]
                new_lp = p + log2(prob)
                if new_lp > max_prob:
                    max_prob = new_lp
                    result = tag_sent

        return result


class MLHMM(HMM):

    def __init__(self, n, tagged_sents, addone=True):
        """
        n -- order of the model.
        tagged_sents -- training sentences, each one being a list of pairs.
        addone -- whether to use addone smoothing (default: True).
        """
        self.n = n
        self.tagged_sents = tagged_sents
        self.tcounts = tcounts = defaultdict(int)
        self.counts = counts = defaultdict(int)
        self.addone = addone

        sents = [list(zip(*x))[0] for x in tagged_sents]
        tags = [list(zip(*x))[1] for x in tagged_sents]

        for tagged_sent in tagged_sents:
            for w, t in tagged_sent:
                counts[w, t] += 1

        for tag in tags:
            for i in range(len(tag) - n + 1):
                ngram = tuple(tag[i: i + n])
                tcounts[ngram] += 1
                tcounts[ngram[:-1]] += 1

        self.words_vocabulary = {word for sent in sents for word in sent}
        self.tags_vocabulary = {tag for sent_tag in tags for tag in sent_tag}

        # super().__init__(n, tagset, trans, out)

    def tcount(self, tokens):
        """Count for an n-gram or (n-1)-gram of tags.

        tokens -- the n-gram or (n-1)-gram tuple of tags.
        """
        return self.tcounts[tuple(tokens)]

    def trans_prob(self, tag, prev_tags):
        """Probability of a tag.

        tag -- the tag.
        prev_tags -- tuple with the previous n-1 tags (optional only if n = 1).
        """
        # q(Yi | Yi-1, Yi-2, ...Yi-k)
        if not prev_tags:
            prev_tags = []

        tags = [tag] + prev_tags

        V = len(self.tags_vocabulary)

        if self.addone:
            num = self.tcounts[tuple(tags)] + 1
            den = self.tcounts[tuple(tags)] + V
        else:
            num = self.tcounts[tuple(tags)]
            den = self.tcounts[tuple(tags)]

        return num / den

    def out_prob(self, word, tag):
        """Probability of a word given a tag.

        word -- the word.
        tag -- the tag.
        """
        # e(word| tag)

        if self.unknown(word):
            return 1 / len(self.words_vocabulary)
        else:
            num = self.counts[word, tag]
            den = self.tcounts[tuple(tag)]

        if den == 0:
            return 0
        return num / den

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return w in self.vocabulary

        """
        Todos los métodos de HMM.
        """
