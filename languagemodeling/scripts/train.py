"""Train an n-gram model.

Usage:
  train.py -n <n> -o <file> [ -m <model> ]
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -m <model>    Model to use [default: ngram]:
                ngram: Unsmoothed n-grams.
                addone: N-grams with add-one smoothing.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
from nltk.corpus import PlaintextCorpusReader, RegexpTokenizer
from languagemodeling.ngram import NGram, AddOneNGram


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    pattern = r'''(?ix)    # set flag to allow verbose regexps
          (?:sr\.|sra\.)
        | (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
        | \w+(?:-\w+)*        # words with optional internal hyphens
        | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
        | \.\.\.            # ellipsis
        | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
    '''
    tokenizer = RegexpTokenizer(pattern)

    root = 'corpus'
    filename = 'juego2.txt'
    corpus = PlaintextCorpusReader(root, '.*\.txt', word_tokenizer=tokenizer)

    # corpus = PlaintextCorpusReader('corpus/',
    #                                '.*\.txt', word_tokenizer=tokenizer)

    sents = corpus.sents()

    # train the model
    n = int(opts['-n'])

    if opts['-m'] == 'addone':
        model = AddOneNGram(n, sents)
    else:
        model = NGram(n, sents)

    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
