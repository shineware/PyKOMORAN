import os

from PyKomoran import jvm
from PyKomoran.type import Pair
from PyKomoran.type import Token

__all__ = ['Komoran']


class KomoranError(Exception):
    """
    Handle exceptions occur in Komoran Class
    """

    def __init__(self, args=None, cause=None):
        super(KomoranError, self).__init__(args)
        self.cause = cause


class Komoran:
    """
    Komoran Wrapper class
    """

    def __init__(self, model_path="./models_full"):
        self._base_path = os.path.dirname(os.path.realpath(__file__))
        self._model_path = os.path.abspath(os.path.join(self._base_path, model_path))

        assert os.path.exists(self._model_path)

        jvm.init_jvm()
        self._komoran = jvm.get_jvm().kr.co.shineware.nlp.pykomoran.KomoranEntryPoint()

        self._komoran.init(self._model_path)
        if not self._komoran.isInitialized():
            raise KomoranError("Komoran is NOT initialized!")

    def _validate_initialized(func):
        def wrapper(self, *args, **kwargs):
            if not self._komoran.isInitialized():
                raise KomoranError("Komoran is NOT initialized!")
            return func(self, *args, **kwargs)

        return wrapper

    @_validate_initialized
    def set_user_dic(self, dic_path):
        self._komoran.setUserDic(dic_path)

    @_validate_initialized
    def set_fw_dic(self, dic_path):
        self._komoran.setFWDic(dic_path)

    @_validate_initialized
    def get_nouns(self, sentence):
        self._komoran.analyze(sentence)
        return list(self._komoran.getNouns())

    @_validate_initialized
    def get_morphes_by_tags(self, sentence, tag_list=list()):
        self._komoran.analyze(sentence)
        return list(self._komoran.getMorphesByTags(tag_list))

    @_validate_initialized
    def get_plain_text(self, sentence):
        self._komoran.analyze(sentence)
        return str(self._komoran.getPlainText())

    @_validate_initialized
    def get_token_list(self, sentence, flatten=True, use_pos_name=False):
        self._komoran.analyze(sentence)
        token_dict_array = self._komoran.getTokenList()
        tokens = [Token(token, use_pos_name=use_pos_name) for token in token_dict_array]

        if flatten:
            return list(tokens)

        tokens_separated = list()
        eojeol = list()
        for idx, token in enumerate(tokens):
            if idx > 0 and tokens[idx - 1].get_end_index() < token.get_begin_index() and eojeol:
                tokens_separated.append(eojeol)
                eojeol = list()
            eojeol.append(token)
        tokens_separated.append(eojeol)

        return tokens_separated

    @_validate_initialized
    def get_list(self, sentence):
        self._komoran.analyze(sentence)
        pair_dict_array = self._komoran.getList()
        pair_array = [Pair(pair) for pair in pair_dict_array]

        return list(pair_array)


if __name__ == '__main__':
    komoran = Komoran()
    str_to_analyze = "① 대한민국은 민주공화국이다. ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."

    print(komoran.get_nouns(str_to_analyze))
    print(komoran.get_morphes_by_tags(str_to_analyze, tag_list=['NNP', "NNG", "SF", "NN", "123"]))
    print(komoran.get_morphes_by_tags(str_to_analyze))
    print(komoran.get_plain_text(str_to_analyze))
    print(komoran.get_token_list(str_to_analyze))
    print(komoran.get_token_list(str_to_analyze, flatten=False))
    print(komoran.get_token_list(str_to_analyze, flatten=False, use_pos_name=True))
    print(komoran.get_list(str_to_analyze))
