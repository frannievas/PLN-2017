"""Train an n-gram model.

Usage:
  train.py -n <n> -o <file> [ -m <model> [-g <gamma>] ]
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -m <model>    Model to use [default: ngram]:
                ngram: Unsmoothed n-grams.
                addone: N-grams with add-one smoothing.
                inter: InterpolatedNGram.
                interaddone: InterpolatedNGram with addone smoothing.
  -g <gamma>    Gamma for InterpolatedNGram
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
from nltk.corpus import PlaintextCorpusReader, RegexpTokenizer
from languagemodeling.ngram import NGram, AddOneNGram, InterpolatedNGram


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

    root = '.'
    corpus = PlaintextCorpusReader(root, 'books\.txt', word_tokenizer=tokenizer)

    sents = corpus.sents()

    # train the model
    n = int(opts['-n'])

    if opts['-m'] == 'addone':
        model = AddOneNGram(n, sents)
    elif opts['-m'] == 'inter':
        gamma = opts['-g']
        if gamma is None:
            model = InterpolatedNGram(n, sents, None, False)
        else:
            model = InterpolatedNGram(n, sents, gamma, False)
    elif opts['-m'] == 'interaddone':
        gamma = opts['-g']
        if gamma is None:
            model = InterpolatedNGram(n, sents, None, True)
        else:
            model = InterpolatedNGram(n, sents, gamma, True)
    else:
        model = NGram(n, sents)

    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
