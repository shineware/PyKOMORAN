import nose
from PyKomoran.type import *


def test_to_init_Token():
    """
    Type Test: init Token using given Dict, and validate given values with Token methods
    :return:
    """
    # @formatter:off
    token = Token({
                'morph': '테스트',
                'pos': 'NNP',
                'beginIndex': 0,
                'endIndex': 3
            })
    # @formatter:on

    assert token.get_morph() == '테스트'
    assert token.get_pos() == 'NNP'
    assert token.get_begin_index() == 0
    assert token.get_end_index() == 3
    assert str(token) == '테스트/NNP(0,3)'
    # @formatter:off
    assert token == Token({
                'morph': '테스트',
                'pos': 'NNP',
                'beginIndex': 0,
                'endIndex': 3
            })
    # @formatter:on


def test_to_init_Token_using_Pos_name():
    """
    Type Test: init Token using given Dict with use_pos_name parameter, and validate given values with Token methods
    :return:
    """
    # @formatter:off
    token = Token({
                'morph': '테스트',
                'pos': 'NNP',
                'beginIndex': 0,
                'endIndex': 3
            }, use_pos_name=True)
    # @formatter:on

    assert token.get_morph() == '테스트'
    assert token.get_pos() == '고유 명사'
    assert token.get_begin_index() == 0
    assert token.get_end_index() == 3
    assert str(token) == '테스트/고유 명사(0,3)'
    # @formatter:off
    assert token == Token({
                        'morph': '테스트',
                        'pos': 'NNP',
                        'beginIndex': 0,
                        'endIndex': 3
                    })
    # @formatter:on


def test_to_init_Pair():
    """
    Type Test: init Pair using given Dict, and validate given values with Pair methods
    :return:
    """
    # @formatter:off
    pair = Pair({
                'first': '테스트',
                'second': 'NNP'
            })
    # @formatter:on

    assert pair.get_first() == '테스트'
    assert pair.get_second() == 'NNP'
    assert str(pair) == '테스트/NNP'
    # @formatter:off
    assert pair == Pair({
                        'first': '테스트',
                        'second': 'NNP'
                    })
    # @formatter:on


def test_to_pos_table():
    """
    Type Test: check pos_table is initialized well
    :return:
    """
    pos_table = Pos()

    assert len(pos_table) == 45
    assert pos_table['NNP'] == '고유 명사'
    assert 'NA' in pos_table
    assert 'ABC' not in pos_table


if __name__ == '__main__':
    nose.runmodule()
