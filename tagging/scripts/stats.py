"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
from prettytable import PrettyTable

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

    words, taggs = zip(*[ x for sent in sents for x in sent])
    print('-> total words: {}'.format(len(words)))

    vocabulary_of_words = { x for x in words}
    vocabulary_of_taggs = { tagg for tagg in taggs}
    print('-> vocabulary of words: {}'.format(len(vocabulary_of_words)))
    print('-> vocabulary of taggs: {}'.format(len(vocabulary_of_taggs)))

    counter_taggs = Counter(taggs)
    total_taggs = len(taggs)
    most_common_taggs = counter_taggs.most_common()[:10]

    # t = taggs c = counts
    t, c = zip(*most_common_taggs)

    # dict_words_most_common["TAGG"] = [ "word1", "word2", "word3"]
    dict_words_most_common = defaultdict(list)
    for sent in sents:
        for a, b in sent:
            if b in t:
                dict_words_most_common[b].append(a)

    # w["tagg"] = "5 most common words" = [(word1, count1), (word2, count2)...]
    w = defaultdict(list)
    for t in dict_words_most_common.keys():
        w[t] = Counter(dict_words_most_common[t]).most_common()[:5]


    print("\nTagg" + "\t" + "Counts" + "\t" + "percent" + "\t\t\t " + "words")
    for a, b in most_common_taggs:
        words = [a for a, b in w[a]]
        print(str(a) + "  | " + str(b) + "  | " + str((b/total_taggs) * 100) +  "  | " + str(words))


    t = PrettyTable(["Tagg", "Counts", "percent", "Words"])
    for a, b in most_common_taggs:
        row = [str(a), str(b), str((b/total_taggs) * 100), str([a for a, b in w[a]]) ]
        t.add_row(row)
    print(t)
