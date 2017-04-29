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
        return self.trans[prev_tags][tag]

    def out_prob(self, word, tag):
        """Probability of a word given a tag.

        word -- the word.
        tag -- the tag.
        """
        # TODO: probabilidad de una palabra dado un tagg
        # TODO: else 0
        return self.out[tag][word]

    def tag_prob(self, y):
        """
        Probability of a tagging.
        Warning: subject to underflow problems.

        y -- tagging.
        """
        # TODO: Dado una secuencia de taggs devuelve su probabilidad
        prob = 0.0
        prev_tags = self.start_tag*(n-1)
        y_extended = y + self.end_tag

        for tagg in y_extended:
            prob *= self.trans_prob(tag, context)

            # Delete 1 prev_tags and add the "tagg"
            if self._n > 1:
                context = context[1:] + (tagg,)



    def prob(self, x, y):
        """
        Joint probability of a sentence and its tagging.
        Warning: subject to underflow problems.

        x -- sentence.
        y -- tagging.
        """

    def tag_log_prob(self, y):
        """
        Log-probability of a tagging.

        y -- tagging.
        """

    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.

        x -- sentence.
        y -- tagging.
        """

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
