# https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log

# N-grama se utiliza n-1 palabras para calcular las probs.
class NGram(object):


    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self.n = n
        self.counts = counts = defaultdict(int)
        self.start_tag = ["<s>"]
        self.end_tag = ["</s>"]


        # Old version
        # if n != 1:
        #     sents = [ ["<s>"] + x for x in sents ]
        # sents = [ x + ["</s>"] for x in sents ]

        for sent in sents:
            # For each sentence
            # Add n-1 start_tags at the beginning (for a n model).
            # Add one end_tag.
            sent_tag = self.start_tag*(n-1) + sent + self.end_tag

            for i in range(len(sent_tag) - n + 1):
                ngram = tuple(sent_tag[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1


    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self.n
        if not prev_tokens:
            prev_tokens = []
        assert len(prev_tokens) == n - 1

        tokens = prev_tokens + [token]
        if self.counts[tuple(prev_tokens)] == 0:
            return 0
        else:
            return float(self.counts[tuple(tokens)]) / self.counts[tuple(prev_tokens)]

    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.

        tokens -- the n-gram or (n-1)-gram tuple.
        """
        return self.counts[tuple(tokens)]

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """
        prob = 1.0
        # Add n-1 start_tags at the beginning (for a n model).
        # Add one end_tag.
        sent_tag = self.start_tag*(self.n-1) + sent + self.end_tag

        for i in range(self.n-1, len(sent_tag)):
            # Unigram Model
            if self.n == 1:
                prob *= self.cond_prob(sent_tag[i])
            else:
                # n > 1
                # i-(n-1) = i + 1 - n
                prob *= self.cond_prob(sent_tag[i],sent_tag[i-(self.n-1):i])
                # print(sent_tag[i])
                # print(sent_tag[i+1-self.n:i])
        return prob

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        a = 0
        for word in sent:
            a += log(self.cond_prob(word))
        return a
