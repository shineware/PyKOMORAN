import os

from PyKomoran import jvm
from PyKomoran.type import Pair
from PyKomoran.type import Token

__all__ = ['Komoran']


class KomoranError(Exception):
    def __init__(self, args=None, cause=None):
        super(KomoranError, self).__init__(args)
        self.cause = cause


class Komoran:
    def __init__(self, model_path="./models_full"):
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.model_path = os.path.join(self.base_path, model_path)

        assert os.path.exists(self.model_path)

        jvm.init_jvm()

        self._komoran = jvm.get_jvm().kr.co.shineware.nlp.pykomoran.KomoranEntryPoint()
        self._komoran.init(model_path)

    def set_user_dic(self, dic_path):
        self._komoran.setUserDic(dic_path)

    def set_fw_dic(self, dic_path):
        self._komoran.setFWDic(dic_path)

    def analyze(self, sentence):
        self._komoran.analyze(sentence)

    def get_nouns(self):
        return self._komoran.getNouns()

    def get_morphes_by_tags(self, tag_list):
        return self._komoran.getMorphesByTags(tag_list)

    def get_plaint_text(self):
        return self._komoran.getPlainText()

    def get_token_list(self, flatten=True):
        token_dict_array = self._komoran.getTokenList()
        tokens = [Token(token) for token in token_dict_array]

        if flatten:
            return tokens

        tokens_separated = list()
        eojeol = list()
        for idx, token in enumerate(tokens):
            if idx > 0 and tokens[idx - 1].get_end_index() < token.get_begin_index() and eojeol:
                tokens_separated.append(eojeol)
                eojeol = list()
            eojeol.append(token)
        tokens_separated.append(eojeol)

        return tokens_separated

    def get_list(self):
        pair_dict_array = self._komoran.getList()
        pair_array = [Pair(pair) for pair in pair_dict_array]

        return pair_array


if __name__ == '__main__':
    komoran = Komoran()

    print(komoran)
    print(komoran.analyze("① 대한민국은 민주공화국이다. ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."))
    print(komoran.get_nouns())
    print(komoran.get_morphes_by_tags(["NNG", "EF", "SF"]))
    print(komoran.get_plaint_text())
    print(komoran.get_token_list())
    print(komoran.get_token_list(flatten=False))
    print(komoran.get_list())
