import os

__all__ = ['Token', 'Pair', 'Pos', 'DEFAULT_MODEL']


class Token:
    """Komoran(Java)의 Token Class에 대응합니다. 형태소 분석 결과 저장을 위해 사용합니다.

    Args:
        token_in_dict (dict): Token으로 만들 Dict
        use_pos_name (bool): Token 출력 시 품사 이름 사용 여부 (기본값: ``False``) \n
                            ``True`` 인 경우 품사 기호 대신 품사 이름을 사용합니다. \n
                            ``False`` 인 경우 품사 기호를 사용합니다.

    Examples:

        >>> # komoran은 Komoran 객체입니다.
        >>> tokens = komoran.get_token_list("① 대한민국은 민주공화국이다.")
        >>> token = tokens[1]
        >>> token
        대한민국/NNP(2,6)
        >>> token.get_morph()
        '대한민국'
        >>> token.get_pos()
        'NNP'
        >>> token.get_begin_index()
        2
        >>> token.get_end_index()
        6

    """
    def __init__(self, token_in_dict, use_pos_name=False):
        self.pos_table = Pos()
        self.morph = token_in_dict.get('morph')
        self.pos = token_in_dict.get('pos')
        self.begin_index = token_in_dict.get('beginIndex')
        self.end_index = token_in_dict.get('endIndex')
        self.use_pos_name = use_pos_name

    def get_morph(self):
        """형태소를 반환합니다.

        Returns:
            str: 형태소
        """
        return self.morph

    def get_pos(self):
        """품사를 반환합니다.

        Returns:
            str: 품사 기호 (또는 이름)
        """
        if self.use_pos_name:
            return self.pos_table[self.pos]
        return self.pos

    def get_begin_index(self):
        """형태소의 시작 인덱스를 반환합니다.

        Returns:
            int: 시작 인덱스
        """
        return self.begin_index

    def get_end_index(self):
        """형태소의 종료 인덱스를 반환합니다.

        Returns:
            int: 종료 인덱스
        """
        return self.end_index

    def __eq__(self, other):
        return (self.morph == other.get_morph()
                and self.pos == other.get_pos()
                and self.begin_index == other.get_begin_index()
                and self.end_index == other.get_end_index())

    def __str__(self):
        return "{0}/{1}({2},{3})".format(self.morph, self.get_pos(), self.begin_index, self.end_index)

    def __repr__(self):
        return self.__str__()


class Pair:
    """Komoran(Java)의 Pair Class에 대응합니다. 형태소 분석 결과 저장을 위해 사용합니다.

    Args:
        pair_in_dict (dict): Pair로 만들 Dict

    Examples:

        >>> # komoran은 Komoran 객체입니다.
        >>> pairs = komoran.get_list("① 대한민국은 민주공화국이다.")
        >>> pair = pairs[1]
        >>> pair
        대한민국/NNP
        >>> pair.get_first()
        '대한민국'
        >>> pair.get_second()
        'NNP'

    """
    def __init__(self, pair_in_dict):
        self.first = pair_in_dict.get('first')
        self.second = pair_in_dict.get('second')

    def get_first(self):
        """형태소를 반환합니다.

        Returns:
            str: 형태소
        """
        return self.first

    def get_second(self):
        """품사를 반환합니다.

        Returns:
            str: 품사 기호
        """
        return self.second

    def __eq__(self, other):
        return (self.first == other.get_first()
                and self.second == other.get_second())

    def __str__(self):
        return "{0}/{1}".format(self.first, self.second)

    def __repr__(self):
        return self.__str__()


class Pos:
    """형태소 분석 결과로 나올 수 있는 모든 품사들에 대한 정보를 갖고 있습니다. \n
    전체 품사표는 :doc:`/firststep/postypes` 를 참고해주세요.

    Examples:

        >>> pos_table = Pos()
        >>> pos['NNP']
        '고유 명사'
        >>> pos['SW']
        '기타기호(논리수학기호,화폐기호)'
        >>> len(pos_table)
        45

    """
    def __init__(self):
        self.pos_table = {
            # 체언
            'NNG': '일반 명사',
            'NNP': '고유 명사',
            'NNB': '의존 명사',
            'NP': '대명사',
            'NR': '수사',

            # 용언
            'VV': '동사',
            'VA': '형용사',
            'VX': '보조 용언',
            'VCP': '긍정 지정사',
            'VCN': '부정 지정사',

            # 수식언
            'MM': '관형사',
            'MAG': '일반 부사',
            'MAJ': '접속 부사',

            # 독립언
            'IC': '감탄사',

            # 관계언
            'JKS': '주격 조사',
            'JKC': '보격 조사',
            'JKG': '관형격 조사',
            'JKO': '목적격 조사',
            'JKB': '부사격 조사',
            'JKV': '호격 조사',
            'JKQ': '인용격 조사',
            'JX': '보조사',
            'JC': '접속 조사',

            # 의존형태
            'EP': '선어말 어미',
            'EF': '종결 어미',
            'EC': '연결 어미',
            'ETN': '명사형 전성 어미',
            'ETM': '관형형 전성 어미 ',
            'XPN': '체언 접두사',
            'XSN': '명사 파생 접미사',
            'XSV': '동사 파생 접미사',
            'XSA': '형용사 파생 접미사',
            'XR': '어근',

            # 기호
            'SF': '마침표,물음표,느낌표',
            'SP': '쉼표,가운뎃점,콜론,빗금',
            'SS': '따옴표,괄호표,줄표',
            'SE': '줄임표',
            'SO': '붙임표(물결,숨김,빠짐)',
            'SL': '외국어',
            'SH': '한자',
            'SW': '기타기호(논리수학기호,화폐기호)',
            'NF': '명사추정범주',
            'NV': '용언추정범주',
            'SN': '숫자',
            'NA': '분석불능범주'
        }
        self.pos_type = self.pos_table.keys()
        self.pos_size = len(self.pos_type)

    def __getitem__(self, pos):
        if pos in self.pos_type:
            return self.pos_table[pos]
        else:
            return ''

    def __len__(self):
        return self.pos_size

    def __contains__(self, pos):
        return pos in self.pos_type

    def __iter__(self):
        return iter(self.pos_table)

    def __str__(self):
        return str(self.pos_table)

    def __repr__(self):
        return repr(self.pos_table)

    def values(self):
        return self.pos_table.values()

    def keys(self):
        return self.pos_table.keys()

    def items(self):
        return self.pos_table.items()

    def has_key(self, key):
        return key in self.pos_type


class DefaultModel:
    def __init__(self):
        base_path = os.path.dirname(os.path.realpath(__file__))

        self._models = {
            'FULL': '{0}{1}models_full'.format(base_path, os.sep),
            'LIGHT': "{0}{1}models_light".format(base_path, os.sep)
        }

    def __getitem__(self, model):
        if model in self._models.keys():
            return self._models[model]
        else:
            return ''

    def __contains__(self, model):
        return model in self._models

    def __str__(self):
        return str(self._models)

    def __repr__(self):
        return repr(self._models)

DEFAULT_MODEL = DefaultModel()