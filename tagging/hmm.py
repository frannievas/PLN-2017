from math import log2


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
        if self._n == 1:
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
        prob = 0.0
        n = self.n
        prev_tags = self.start_tag*(n-1)
        y_extended = y + self.end_tag

        for tag in y_extended:
            prob *= self.trans_prob(tag, prev_tags)

            # Delete 1 prev_tags and add the "tagg"
            if self._n > 1:
                prev_tags = prev_tags[1:] + (tag,)

        return prob

    def prob(self, x, y):
        """
        Joint probability of a sentence and its tagging.
        Warning: subject to underflow problems.

        x -- sentence.
        y -- tagging.
        """

        prob = 0.0
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
        prev_tags = self.start_tag*(n-1)
        y_extended = y + self.end_tag

        for tag in y_extended:
            prob = self.trans_prob(tag, prev_tags)

            # Delete 1 prev_tags and add the "tagg"
            if self._n > 1:
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


class ViterbiTagger:

    def __init__(self, hmm):
        """
        hmm -- the HMM.
        """

    def tag(self, sent):
        """Returns the most probable tagging for a sentence.

        sent -- the sentence.
        """
