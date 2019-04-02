import os
from functools import wraps

from PyKomoran import jvm
from PyKomoran.type import Pair
from PyKomoran.type import Token

__all__ = ['Komoran']


class KomoranError(Exception):
    """
    Komoran Class에서 발생하는 예외상황을 위한 Exception
    Handle exceptions occur in Komoran Class
    """

    def __init__(self, args=None, cause=None):
        super(KomoranError, self).__init__(args)
        self.cause = cause


class Komoran:
    """Komoran(Java)의 Python Wrapper Class입니다.

    Args:
        model_path (str): Komoran 객체 초기화를 위한 model path (절대 경로)
        max_heap (int): JVM의 Max Heap Size (기본값: ``1024``, 단위: ``MB``)

    Examples:
        기본 모델(FULL, LIGHT) 외에 사용자가 직접 생성한 모델이 존재하는 곳의 ``절대 경로`` 를 이용하여 Komoran 객체를 생성할 수 있습니다.

        >>> # DEFAULT_MODEL.FULL 로 Komoran 객체를 생성합니다.
        >>> komoran_full = Komoran()
        >>> # DEFAULT_MODEL.LIGHT 로 Komoran 객체를 생성합니다.
        >>> komoran_light = Komoran("./models_light")
        >>> # 사용자가 미리 생성 모델로 Komoran 객체를 생성합니다.
        >>> komoran_user = Komoran("/home/user/Komoran/Model")

    """

    def __init__(self, model_path="./models_full", max_heap=1024):
        self._base_path = os.path.dirname(os.path.realpath(__file__))
        self._model_path = os.path.abspath(os.path.join(self._base_path, model_path))

        assert os.path.exists(self._model_path)

        jvm.init_jvm(max_heap)
        self._komoran = jvm.get_jvm().kr.co.shineware.nlp.pykomoran.KomoranEntryPoint()

        self._komoran.init(self._model_path)
        if not self._komoran.isInitialized():
            raise KomoranError("Komoran is NOT initialized!")

    def _validate_initialized(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self._komoran.isInitialized():
                raise KomoranError("Komoran is NOT initialized!")
            return func(self, *args, **kwargs)

        return wrapper

    @_validate_initialized
    def set_user_dic(self, dic_path):
        """사용자 사전을 적용합니다.

        Args:
            dic_path (str): 사용자 사전이 존재하는 경로 (절대 경로)
        """
        if not os.path.exists(dic_path):
            raise KomoranError("user.dic path does NOT exist!")
        self._komoran.setUserDic(dic_path)

    @_validate_initialized
    def set_fw_dic(self, dic_path):
        """기분석 사전을 적용합니다.

        Args:
            dic_path (str): 기분석 사전이 존재하는 경로 (절대 경로)
        """
        if not os.path.exists(dic_path):
            raise KomoranError("fw.dic path does NOT exist!")
        self._komoran.setFWDic(dic_path)

    @_validate_initialized
    def get_nouns(self, sentence):
        """입력 문장의 형태소 분석 결과 중, 명사류만 반환합니다.

        Args:
            sentence (str): 분석할 문장

        Returns:
            list: 입력 문장의 명사류에 해당하는 형태소(str) List

        Examples:

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_nouns("① 대한민국은 민주공화국이다.")
            ['대한민국', '민주공화국']

        """
        self._komoran.analyze(sentence)
        return list(self._komoran.getNouns())

    @_validate_initialized
    def get_morphes_by_tags(self, sentence, tag_list=list()):
        """입력 문장의 형태소 분석 결과 중, 주어진 품사들만 반환합니다.

        Args:
            sentence (str): 분석할 문장
            tag_list (list): 반환받을 품사 목록 (기본값: ``[]`` )

        Returns:
            list: 입력 문장의 주어진 품사들에 해당하는 형태소(str) List

        Examples:

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_morphes_by_tags("① 대한민국은 민주공화국이다.", tag_list=['NNP', 'NNG', 'SF'])
            ['대한민국', '민주공화국', '.']
            >>> # tag_list를 지정하지 않으면(=빈 List를 tag_list로 제공하면) 아무런 형태소도 반환하지 않습니다.
            >>> komoran.get_morphes_by_tags("① 대한민국은 민주공화국이다.", tag_list=[])
            []

        """
        self._komoran.analyze(sentence)
        return list(self._komoran.getMorphesByTags(tag_list))

    @_validate_initialized
    def get_plain_text(self, sentence):
        """입력 문장의 형태소 분석 결과를 품사 태깅된 형태로 반환합니다.

        Args:
            sentence (str): 분석할 문장

        Returns:
            str: 입력 문장에 형태소 별로 품사 태깅된 형태

        Examples:

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_plain_text("① 대한민국은 민주공화국이다.")
            '①/SW 대한민국/NNP 은/JX 민주공화국/NNP 이/VCP 다/EF ./SF'

        """
        self._komoran.analyze(sentence)
        return str(self._komoran.getPlainText())

    @_validate_initialized
    def get_token_list(self, sentence, flatten=True, use_pos_name=False):
        """입력 문장의 형태소 분석 결과를 Token(:meth:`PyKomoran.type.Token`) 목록으로 반환합니다.

        Args:
            sentence (str): 분석할 문장
            flatten (bool): 어절 무시 여부 (기본값: ``True``)
                            | ``True`` 인 경우 어절을 무시하고 하나의 List로 반환합니다.
                            | ``False`` 인 경우 어절별로 List를 만들어 List of List로 반환합니다.
            use_pos_name (bool): 품사 이름 사용 여부 (기본값: ``False``)
                                | ``True`` 인 경우 품사 기호 대신 품사 이름을 사용합니다.
                                | ``False`` 인 경우 품사 기호를 사용합니다.

        Returns:
            list: 형태소 Token(:meth:`PyKomoran.type.Token`)의 List

        Examples:

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_token_list("① 대한민국은 민주공화국이다.")
            [①/SW(0,1), 대한민국/NNP(2,6), 은/JX(6,7), 민주공화국/NNP(8,13), 이/VCP(13,14), 다/EF(14,15), ./SF(15,16)]
            >>> komoran.get_token_list("① 대한민국은 민주공화국이다.", flatten=False)
            [[①/SW(0,1)], [대한민국/NNP(2,6), 은/JX(6,7)], [민주공화국/NNP(8,13), 이/VCP(13,14), 다/EF(14,15), ./SF(15,16)]]
            >>> komoran.get_token_list("① 대한민국은 민주공화국이다.", use_pos_name=True)
            [①/기타기호(논리수학기호,화폐기호)(0,1), 대한민국/고유 명사(2,6), 은/보조사(6,7), 민주공화국/고유 명사(8,13), 이/긍정 지정사(13,14), 다/종결 어미(14,15), ./마침표,물음표,느낌표(15,16)]

        """
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
        """입력 문장의 형태소 분석 결과를 Pair(:meth:`PyKomoran.type.Pair`) 목록으로 반환합니다.

        Args:
            sentence (str): 분석할 문장

        Returns:
            list: 형태소 Pair(:meth:`PyKomoran.type.Pair`)의 List

        Examples:

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_list("① 대한민국은 민주공화국이다.")
            [①/SW, 대한민국/NNP, 은/JX, 민주공화국/NNP, 이/VCP, 다/EF, ./SF]

        """
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
