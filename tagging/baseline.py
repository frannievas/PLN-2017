from collections import Counter, defaultdict


class BaselineTagger:

    def __init__(self, tagged_sents):
        """
        Programar un etiquetador baseline, que elija para cada palabra su
        etiqueta más frecuente observada en entrenamiento.
        Para las palabras desconocidas, devolver la etiqueta 'nc0s000'.

        tagged_sents -- training sentences, each one being a list of pairs.
        """

        all_words = [word for sent in tagged_sents for word in sent]
        counter = Counter(all_words)

        max_counts = defaultdict(int)
        self.taggs = taggs = defaultdict(str)
        for w, t in counter.keys():
            if max_counts[w] < counter[(w, t)]:
                max_counts[w] = counter[(w, t)]
                taggs[w] = t

        self.unk_tagg = "nc0s000"
        self.counts = max_counts

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]

    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """

        if self.unknown(w):
            return self.unk_tagg
        return self.taggs[w]

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return w not in self.counts
