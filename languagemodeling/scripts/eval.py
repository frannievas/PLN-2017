"""
Evaulate a language model using the test set.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Language model file.
  -h --help     Show this screen.
"""
from nltk.corpus import PlaintextCorpusReader, RegexpTokenizer
from docopt import docopt
import pickle

if __name__ == '__main__':
    opts = docopt(__doc__)

    pattern = r'''(?ix)    # set flag to allow verbose regexps
          (?:sr\.|sra\.)
        | (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
        | \w+(?:-\w+)*        # words with optional internal hyphens
        | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
        | \.\.\.            # ellipsis
        | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
    '''
    tokenizer = RegexpTokenizer(pattern)
    root = 'corpus_eval'
    filename = 'eval.txt'
    corpus = PlaintextCorpusReader(root, filename, word_tokenizer=tokenizer)
    sents = corpus.sents()

    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    print("Perplexity: {}".format(model.perplexity(sents)))
    print("Cross-entropy: {}".format(model.cross_entropy(sents)))
