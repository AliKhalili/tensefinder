import spacy
from TensFinder.SentenceTenseModel import SentenceTenseModel


class TenseParser:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def find_tenses(self, text):
        doc = self.nlp(text)
        tense_list = []
        # for token in doc:
        #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
        for sentence in doc.sents:
            if len(sentence) <= 1:
                continue
            sentence_tense_model = SentenceTenseModel(sentence)
            tense_list.append(sentence_tense_model.parse())
        return tense_list

    def find_tense_simple_form(self, text):
        result = self.find_tenses(text)
        return [[tense.tense for tense in sentence] for sentence in result]

    def find_tense_simple_form_str(self, text):
        result = self.find_tense_simple_form(text)
        return '. '.join([' '.join([str(tense) for tense in sentence]) for sentence in result])
