"""Train a sequence tagger.

Usage:
  train.py [-m <model> [-n <order> | --a]] -o <file>
  train.py -h | --help

Options:
  -m <model>    Model to use [default: base]:
                  base: Baseline
                  mlhmm: MLHMM
  -n <order>    Order of the model (Only in the MLHMM model)
  --a           Select to use or not Addone (Only in the MLHMM model)
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle

from corpus.ancora import SimpleAncoraCorpusReader
from tagging.baseline import BaselineTagger
from tagging.hmm import MLHMM

models = {
    'base': BaselineTagger,
    'mlhmm': MLHMM,
}


if __name__ == '__main__':
    opts = docopt(__doc__)

    MYPATH = '../../corpus/'
    # load the data
    files = 'CESS-CAST-(A|AA|P)/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader(MYPATH + 'ancora-3.0.1es/', files)
    sents = list(corpus.tagged_sents())

    # train the model
    m = opts['-m']
    if m == 'base':
        model = models[m](sents)
    else:
        model = models[m](int(opts['-n']), sents, True)
    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
