from TensFinder.TenseModel import TenseModel
from TensFinder.TenseSegmentModel import TenseSegmentModel


class SentenceTenseModel:
    def __init__(self, tokens):
        self._tokens = tokens

    def parse(self):
        tense_list = []

        current_tense = []
        increment_counter = 0
        for token in self._tokens:
            if token.pos_ in ('AUX', 'VERB'):
                increment_counter += 1
                tense_segment = TenseSegmentModel(token.text, token.lemma_, token.tag_)
                current_tense.append(tense_segment)
            elif increment_counter > 0:
                increment_counter = 0
                tense = TenseModel(current_tense)
                tense_list.append(tense)
                current_tense = []
        return tense_list
