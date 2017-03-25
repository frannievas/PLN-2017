from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import RegexpTokenizer
if __name__ == '__main__':

    pattern = r'\w'

    tokenizer = RegexpTokenizer(pattern)

    corpus = PlaintextCorpusReader('corpus/', '.*\.txt')

    for sentence in corpus.sents()[100:102]:
        print(sentence)
