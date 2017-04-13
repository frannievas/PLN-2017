# https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log2
from numpy.random import uniform


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

        if n == 1:
            return (float(self.counts[tuple(tokens)]) / self.counts[()])
        if self.counts[tuple(prev_tokens)] == 0:
            return 0
        else:
            return (float(self.counts[tuple(tokens)]) /
                    self.counts[tuple(prev_tokens)])

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
                prob *= self.cond_prob(sent_tag[i], sent_tag[i-(self.n-1):i])
                # print(sent_tag[i])
                # print(sent_tag[i+1-self.n:i])
        return prob

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        # a = 0
        # for word in sent:
        #     a += log(self.cond_prob(word))
        # return a
        log_prob = 0.0
        sent_tag = self.start_tag*(self.n-1) + sent + self.end_tag

        for i in range(self.n-1, len(sent_tag)):
            # Unigram Model
            if self.n == 1:
                prob = self.cond_prob(sent_tag[i])
                if prob > 0:
                    log_prob += log2(prob)
                else:
                    log_prob = float("-inf")
            else:
                # n > 1
                prob = self.cond_prob(sent_tag[i], sent_tag[i-(self.n-1):i])
                if prob > 0:
                    log_prob += log2(prob)
                else:
                    log_prob += float("-inf")

        return log_prob

    def log_prob(self, sents):
        """Compute the sum of the log probabilities of sentences.
        sents -- list of sentences, each one being a list of tokens.
        """
        prob = 0
        for sent in sents:
            prob += self.sent_log_prob(sent)
        return prob

    def perplexity(self, sents):
        """Compute the perplexity of sentences.
        sents -- list of sentences, each one being a list of tokens.
        """
        return 2 ** (-self.cross_entropy(sents))

    def cross_entropy(self, sents):
        """ Compute the cross entropy of the model.
            sents -- list of sentences, each one being a list of tokens.
        """
        words = 0
        for sent in sents:
            words += len(sent)

        cross_entropy = self.log_prob(sents) / words

        return cross_entropy


class NGramGenerator:

    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self.model = model
        n = self.model.n

        ngrams = set()
        for key in model.counts:
            if len(key) == n:
                ngrams.add(key)

        # Create dict of dicts
        self.probs = probs = defaultdict(dict)
        self.sorted_probs = sorted_probs = defaultdict(list)

        for key in ngrams:
                word = key[n-1]
                tail = key[:-1]
                # If doesn't exist the tail, defaultdict create the dict
                probs[tail][word] = model.cond_prob(word, list(tail))

        # Copy prob to sorted_probs
        for p in probs:
            for elem in probs[p]:
                sorted_probs[p].append((elem, probs[tuple(p)][elem]))

        # Sort
        if n > 1:
            for key, words in sorted_probs.items():
                words.sort(key=lambda p: p[1])
                words.sort(key=lambda p: p[0])
        else:
            sorted_probs[()].sort(key=lambda p: p[1])
            sorted_probs[()].sort(key=lambda p: p[0])

    def generate_sent(self):
        """Randomly generate a sentence."""

        prev_tokens = (self.model.n-1)*self.model.start_tag
        sentence = []

        word = self.generate_token(tuple(prev_tokens))

        # While don't generate the end_tag, keep generating words
        while word != self.model.end_tag[0]:
            sentence.append(word)
            if self.model.n > 1:
                # Update the prev_tokens
                prev_tokens = prev_tokens[1:] + [word]
            word = self.generate_token(tuple(prev_tokens))

        return sentence

    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.

        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        list_tokens = self.sorted_probs[prev_tokens]
        s = sum(w for c, w in list_tokens)
        r = uniform(0, s)
        prob = 0
        word = ""

        for elem, p in list_tokens:
            if prob + p > r:
                word = elem
                break
            else:
                prob += p

        return word


class AddOneNGram(NGram):

    """
       Todos los métodos de NGram.
    """
    def __init__(self, n, sents):
        super().__init__(n, sents)
        self.n = n
        self.word_set = word_set = set()

        for sent in sents:
            for word in sent:
                word_set.add(word)

        word_set.add(self.end_tag[0])
        self.word_types = len(word_set)

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability add-one of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """

        n = self.n
        if not prev_tokens:
            prev_tokens = []
        assert len(prev_tokens) == n - 1
        tokens = prev_tokens + [token]
        return (float(self.counts[tuple(tokens)] + 1) /
                (self.counts[tuple(prev_tokens)] + self.V()))

    def V(self):
        """Size of the vocabulary.
        """
        return self.word_types
