"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt

from corpus.ancora import SimpleAncoraCorpusReader
from collections import defaultdict, Counter

if __name__ == '__main__':
    opts = docopt(__doc__)

    MYPATH = "../../corpus/"
    # load the data
    corpus = SimpleAncoraCorpusReader(MYPATH + 'ancora-2.0/')
    sents = list(corpus.tagged_sents())

    # compute the statistics
    print('-> sents: {}'.format(len(sents)))

    total_words = sum([len(sent) for sent in sents])
    print('-> total words: {}'.format(total_words))

    words, taggs = zip(*[ x for sent in sents for x in sent])
    print('-> total words: {}'.format(len(words)))

    vocabulary_of_words = { x for x in words}
    vocabulary_of_taggs = { tagg for tagg in taggs}
    print('-> vocabulary of words: {}'.format(len(vocabulary_of_words)))
    print('-> vocabulary of taggs: {}'.format(len(vocabulary_of_taggs)))

    counter_taggs = Counter(taggs)
    most_common_taggs = counter_taggs.most_common()[:10]

    print("\nTagg" + "\t" + "Counts")
    for a, b in most_common_taggs:
        print(str(a) + "  | " + str(b))
