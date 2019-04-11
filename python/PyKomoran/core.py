import os
from functools import wraps

from PyKomoran import jvm
from PyKomoran.type import Pair
from PyKomoran.type import Token
from PyKomoran.type import Pos
from PyKomoran.type import DEFAULT_MODEL

__all__ = ['Komoran']

class KomoranError(Exception):
    """
    Komoran Class에서 발생하는 예외상황을 위한 Exception
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
        기본 모델( ``DEFAULT_MODEL['FULL']`` , ``DEFAULT_MODEL['LIGHT']`` ) 외에 사용자가 직접 생성한 모델이 위치하는
        ``절대 경로`` 를 이용하여 Komoran 객체를 생성할 수 있습니다.

        >>> # 기본으로 제공하는 LIGHT 모델로 Komoran 객체를 생성합니다.
        >>> komoran = Komoran(DEFAULT_MODEL['LIGHT'])
        >>> # 기본으로 제공하는 FULL 모델로 Komoran 객체를 생성합니다.
        >>> komoran = Komoran(DEFAULT_MODEL['FULL'])
        >>> # 사용자가 미리 생성 모델로 Komoran 객체를 생성합니다.
        >>> komoran_user = Komoran("/some/where/path/Komoran/Model")

    """

    def __init__(self, model_path, max_heap=1024):
        if max_heap <= 0:
            raise KomoranError("Heap size for JVM is too small!")

        if not os.path.exists(model_path):
            raise KomoranError("model does NOT exist!")

        self.pos_table = Pos()

        jvm.init_jvm(max_heap)
        self._komoran = jvm.get_jvm().kr.co.shineware.nlp.pykomoran.KomoranEntryPoint()

        self._komoran.init(model_path)
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

        Examples:
            이 예제에서는 사용자 사전 적용 전/후의 형태소 분석 결과를 비교합니다. \n
            사용자 사전이 위치한 경로는 `/Users/9bow/Workspace/KOMORAN/dic.user` 이고, 파일 내용은 아래와 같다고 가정합니다.

            ::

                # 이 파일은 사용자 사전 파일입니다.
                # 입력 문장 내에 사용자 사전에 포함된 내용이 있는 구간에 대해서는 해당 품사를 출력하게 됩니다.
                # 형태소의 품사를 적지 않으면 기본적으로 고유명사(NNP)로 인지합니다.
                샤인웨어	NNP
                TV는 사랑을 싣고	NNP

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_plain_text("샤인웨어에서 단체로 캡틴 마블을 관람했습니다.")
            '샤인/NNP 웨어/NNG 에서/JKB 단체/NNG 로/JKB 캡틴 마블/NNP 을/JKO 관람/NNG 하/XSV 았/EP 습니다/EF ./SF'
            >>> komoran.set_user_dic("/Users/9bow/Workspace/KOMORAN/dic.user")
            >>> komoran.get_plain_text("샤인웨어에서 단체로 캡틴 마블을 관람했습니다.")
            '샤인웨어/NNP 에서/JKB 단체/NNG 로/JKB 캡틴 마블/NNP 을/JKO 관람/NNG 하/XSV 았/EP 습니다/EF ./SF'

        """
        if not os.path.exists(dic_path):
            raise KomoranError("user.dic path does NOT exist!")
        self._komoran.setUserDic(dic_path)

    @_validate_initialized
    def set_fw_dic(self, dic_path):
        """기분석 사전을 적용합니다.

        Args:
            dic_path (str): 기분석 사전이 존재하는 경로 (절대 경로)

        Examples:
            이 예제에서는 사용자 사전 적용 전/후의 형태소 분석 결과를 비교합니다. \n
            사용자 사전이 위치한 경로는 `/Users/9bow/Workspace/KOMORAN/fwd.user` 이고, 파일 내용은 아래와 같다고 가정합니다.

            ::

                # 이 파일은 기분석 사전입니다.
                # 기분석 사전은 어절이 100% 일치하는 경우에만 적용이 됩니다.
                # 분석된 결과의 품사열은 grammar에서 출현 가능한 형태여야 합니다.
                샤인웨어	NNP

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_plain_text("샤인웨어는 자연어 처리를 연구합니다.")
            '샤인/NNP 웨어/NNG 는/JX 자연어/NNP 처리/NNG 를/JKO 연구/NNG 하/XSV ㅂ니다/EF ./SF'
            >>> komoran.set_user_dic("/Users/9bow/Workspace/KOMORAN/fwd.user")
            >>> komoran.get_plain_text("샤인웨어는 자연어 처리를 연구합니다.")
            '샤인웨어/NNP 는/JX 자연어/NNP 처리/NNG 를/JKO 연구/NNG 하/XSV ㅂ니다/EF ./SF'

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
    def get_morphes_by_tags(self, sentence, tag_list=None):
        """입력 문장의 형태소 분석 결과 중, 주어진 품사들만 반환합니다. 주어진 품사가 없을 경우 전체 형태소를 반환합니다.

        Args:
            sentence (str): 분석할 문장
            tag_list (list): 반환받을 품사 목록 (기본값: 전체 형태소)

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
        if tag_list is None:
            tag_list = list(self.pos_table)
        elif not isinstance(tag_list, list):
            raise KomoranError("Param tag_list should be list type")

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
        """입력 문장의 형태소 분석 결과를 :class:`Token <PyKomoran.type.Token>` 의 목록으로 반환합니다.

        Args:
            sentence (str): 분석할 문장
            flatten (bool): 어절 무시 여부 (기본값: ``True``) \n
                            ``True`` 인 경우 어절을 무시하고 하나의 List로 반환합니다. \n
                            ``False`` 인 경우 어절별로 List를 만들어 List of List로 반환합니다.
            use_pos_name (bool): 품사 이름 사용 여부 (기본값: ``False``) \n
                                ``True`` 인 경우 품사 기호 대신 품사 이름을 사용합니다. \n
                                ``False`` 인 경우 품사 기호를 사용합니다.

        Returns:
            list: 형태소 :class:`Token <PyKomoran.type.Token>` 의 List

        Examples:

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_token_list("① 대한민국은 민주공화국이다.")
            [①/SW(0,1), 대한민국/NNP(2,6), 은/JX(6,7), 민주공화국/NNP(8,13), 이/VCP(13,14), 다/EF(14,15), ./SF(15,16)]
            >>> komoran.get_token_list("① 대한민국은 민주공화국이다.", flatten=False)
            [[①/SW(0,1)], [대한민국/NNP(2,6), 은/JX(6,7)], [민주공화국/NNP(8,13), 이/VCP(13,14), 다/EF(14,15), ./SF(15,16)]]
            >>> komoran.get_token_list("① 대한민국은 민주공화국이다.", use_pos_name=True)
            [①/기타기호(논리수학기호,화폐기호)(0,1), 대한민국/고유 명사(2,6), 은/보조사(6,7), 민주공화국/고유 명사(8,13), 이/긍정 지정사(13,14), 다/종결 어미(14,15), ./마침표,물음표,느낌표(15,16)]

        """
        if not isinstance(flatten, bool):
            raise KomoranError("Param flatten should be boolean type")
        elif not isinstance(use_pos_name, bool):
            raise KomoranError("Param use_pos_name should be boolean type")

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
        """입력 문장의 형태소 분석 결과를 :class:`Pair <PyKomoran.type.Pair>` 의 목록으로 반환합니다.

        Args:
            sentence (str): 분석할 문장

        Returns:
            list: 형태소 :class:`Pair <PyKomoran.type.Pair>` 의 List

        Examples:

            >>> # komoran은 Komoran 객체입니다.
            >>> komoran.get_list("① 대한민국은 민주공화국이다.")
            [①/SW, 대한민국/NNP, 은/JX, 민주공화국/NNP, 이/VCP, 다/EF, ./SF]

        """
        self._komoran.analyze(sentence)
        pair_dict_array = self._komoran.getList()
        pair_array = [Pair(pair) for pair in pair_dict_array]

        return list(pair_array)

    @_validate_initialized
    def morphes(self, sentence):
        """konlpy에 익숙한 분들을 위한 :meth:`get_morphes_by_tags() <PyKomoran.core.Komoran.get_morphes_by_tags>` 메소드의 별칭입니다.\n
        전체 형태소를 목록 형태로 반환합니다.
        """
        return self.get_nouns(sentence)

    @_validate_initialized
    def nouns(self, sentence):
        """konlpy에 익숙한 분들을 위한 :meth:`get_nouns() <PyKomoran.core.Komoran.get_nouns>` 메소드의 별칭입니다.\n
        명사 형태소를 목록 형태로 반환합니다.
        """
        return self.get_nouns(sentence)

    @_validate_initialized
    def pos(self, sentence, flatten=True):
        """konlpy에 익숙한 분들을 위한 :meth:`get_token_list() <PyKomoran.core.Komoran.get_token_list>` 메소드의 별칭입니다.\n
        전체 형태소를 :class:`Token <PyKomoran.type.Token>` 의 목록 형태로 반환하기 때문에 `join` 은 사용하지 않습니다.
        """
        return self.get_token_list(sentence, flatten=flatten)


if __name__ == '__main__':
    komoran = Komoran(DEFAULT_MODEL['FULL'])
    str_to_analyze = "① 대한민국은 민주공화국이다. ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."

    print(komoran.get_nouns(str_to_analyze))
    print(komoran.get_morphes_by_tags(str_to_analyze, tag_list=['NNP', "NNG", "SF", "NN", "123"]))
    print(komoran.get_morphes_by_tags(str_to_analyze))
    print(komoran.get_plain_text(str_to_analyze))
    print(komoran.get_token_list(str_to_analyze))
    print(komoran.get_token_list(str_to_analyze, flatten=False))
    print(komoran.get_token_list(str_to_analyze, flatten=False, use_pos_name=True))
    print(komoran.get_list(str_to_analyze))
