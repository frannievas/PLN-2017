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

        start_tag = ["<s>"]
        end_tag = ["</s>"]

        if n != 1:
            counts[tuple(start_tag)] += len(sents)
            sents = [ x + ["</s>"] for x in sents ]

        for sent in sents:
            for i in range(len(sent) - n + 1):
                ngram = tuple(sent[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1

        # Delete "</s>" added in corpus
        sents = [x[:-1] for x in sents]

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
        prob = 1
        for word in range(len(sent)):
             if word + 1 < self.n:
                 prob *= self.cond_prob(word,sent[0:word])
                #  print(sent[word])
                #  print(sent[0:word])
             else:
                 prob = self.cond_prob(word,sent[word+1-self.n:word])
                #  print(sent[word])
                #  print(sent[word+1-n:word])

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        a = 0
        for word in sent:
            a += log(self.prob(word))
        return a
