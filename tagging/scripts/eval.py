"""Evaulate a tagger.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Tagging model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import sys
import numpy

from corpus.ancora import SimpleAncoraCorpusReader
from sklearn.metrics import confusion_matrix

def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the model
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    MYPATH = '../../corpus/'
    # load the data
    files = '3LB-CAST/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader(MYPATH + 'ancora-3.0.1es/', files)
    sents = list(corpus.tagged_sents())

    # tag
    hits, hits_known, hits_unknown, total = 0, 0, 0, 0
    n = len(sents)
    y_test = []
    y_pred = []

    for i, sent in enumerate(sents):
        word_sent, gold_tag_sent = zip(*sent)

        model_tag_sent = model.tag(word_sent)
        y_test += gold_tag_sent
        y_pred += model_tag_sent
        assert len(model_tag_sent) == len(gold_tag_sent), i

        # global score
        hits_sent = [m == g for m, g in zip(model_tag_sent, gold_tag_sent)]
        hits += sum(hits_sent)
        total += len(sent)
        acc = float(hits) / total

        # unknown
        l = len(word_sent)
        pos_unknown = [k for k in range(l) if model.unknown(word_sent[k])]
        hits_unknown_sent = [model_tag_sent[k] == gold_tag_sent[k] for k in pos_unknown]
        hits_unknown += sum(hits_unknown_sent)

        # known
        pos_known = [k for k in range(l) if not model.unknown(word_sent[k])]
        hits_known_sent = [model_tag_sent[k] == gold_tag_sent[k] for k in pos_known]
        hits_known += sum(hits_known_sent)

        progress('{:3.1f}% ({:2.2f}%)'.format(float(i) * 100 / n, acc * 100))

    acc = float(hits) / total
    acc_known = float(hits_known) / total
    acc_unknown = float(hits_unknown) / total

    print('')
    print('Accuracy: {:2.2f}%'.format(acc * 100))
    print('Accuracy Known: {:2.2f}%'.format(acc_known * 100))
    print('Accuracy Unknown: {:2.2f}%'.format(acc_unknown * 100))

    # Confusion matrix.
    cm = confusion_matrix(y_test, y_pred)
    numpy.set_printoptions()
    print("Confusion matrix:")
    print(cm)
