### Trabajo Práctico 1 - Modelado de Lenguaje

- Francisco Nievas
* frannievas@gmail.com

#### Ejercicio 1: Corpus

Como corpus en lenguaje natural se utilizó los textos de los libros de [Game_of_Thrones](https://en.wikipedia.org/wiki/Game_of_Thrones) en español.
Como "corpus reader" se utilizó ```PlaintextCorpusReader``` de la libreria [nltk](http://www.nltk.org/_modules/nltk/corpus/reader/plaintext.html), junto a ```RegexpTokenizer``` que permite utilizar una expreción regular para poder tokenizar y segmentar las oraciones.

La siguiente es la expreción regular que se utilizo:
```python
#
# pattern = r'''(?ix)    # set flag to allow verbose regexps
#       (?:sr\.|sra\.)
#     | (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
#     | \w+(?:-\w+)*        # words with optional internal hyphens
#     | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
#     | \.\.\.            # ellipsis
#     | [][.,;"'?():-_`]  # these are separate tokens; includes ], [
# '''
```
Se procedió a verificar la correcta segmentación, y no hubo necesidad de cambiar la expreción para corregir algun defecto.

#### Ejercicio 2: Modelo de n-gramas
