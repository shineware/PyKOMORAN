""" This test filename has 'a' prefix because this test should run before running other tests """
import nose

from PyKomoran.jvm import *

global jvm_gateway
if jvm_gateway is not None:
    jvm_gateway.shutdown()
test_jvm1 = None


def test_to_before_init_Jvm():
    """
    JVM Test: before jvm_init(), jvm_gateway should be None
    :return:
    """
    global jvm_gateway

    assert jvm_gateway is None


def test_to_get_Jvm_before_init():
    """
    JVM Test: before jvm_init(), get_jvm() should be None
    :return:
    """
    global test_jvm1

    test_jvm1 = get_jvm()

    assert test_jvm1 is None


def test_to_init_Jvm():
    """
    JVM Test: when call jvm_init() first time, jvm object should be returned
    :return:
    """
    global test_jvm1

    test_jvm1 = init_jvm(1024)

    assert test_jvm1 is not None


def test_to_duplicate_init_Jvm():
    """
    JVM Test: when call jvm_init() more than once, None should be returned
    :return:
    """
    global test_jvm1

    test_jvm2 = init_jvm(1024)
    test_jvm3 = init_jvm(1024)

    assert test_jvm1 is not None
    assert test_jvm2 is None
    assert test_jvm3 is None


def test_to_get_Jvm_after_init():
    """
    JVM Test: when call get_jvm() after init_jvm(), jvm object should be returned
    :return:
    """
    test_jvm2 = get_jvm()

    assert test_jvm2 is not None


def test_to_duplicate_get_Jvm_after_init():
    """
    JVM Test: when call get_jvm() after init_jvm() more than once, returned values should be same
    :return:
    """
    global test_jvm1

    test_jvm2 = get_jvm()
    test_jvm3 = get_jvm()

    assert test_jvm1 is not None
    assert test_jvm2 is not None
    assert test_jvm3 is not None
    assert id(test_jvm1) == id(test_jvm2)
    assert id(test_jvm1) == id(test_jvm3)


if __name__ == '__main__':
    nose.runmodule()
