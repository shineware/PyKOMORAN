import os
import logging

from py4j.java_gateway import GatewayParameters
from py4j.java_gateway import JavaGateway
from py4j.java_gateway import launch_gateway

__all__ = ['jvm_gateway', 'init_jvm', 'get_jvm']

jvm_gateway = None


def init_jvm(max_heap=1024, jar_path="./libs"):
    """KOMORAN Jar를 포함한 JVM을 초기화한 후, 반환합니다.

    Args:
        max_heap (int): JVM 실행 시 Max Heap Size (기본값: ``1024``, 단위: ``MB``)
        jar_path (str): JVM 실행 시 포함할 Jar Path 지정 (기본값: ``"./libs"``)

    Returns:
        py4j.java_gateway.JavaGateway: 초기화된 JVM 객체
    """
    base_path = os.path.dirname(os.path.realpath(__file__))
    jar_path = os.path.abspath(os.path.join(base_path, jar_path))

    assert os.path.exists(jar_path)

    global jvm_gateway

    if jvm_gateway is not None:
        return

    libraries = [
        '{0}{1}KOMORAN-3.3.4.jar',
        '{0}{1}KOMORANEntryPoint-0.1.0.jar',
        # '{0}{1}*'
    ]

    classpath = os.pathsep.join([lib.format(jar_path, os.sep) for lib in libraries])
    py4j_path = "{0}{1}py4j0.10.8.1.jar".format(jar_path, os.sep)

    port = launch_gateway(jarpath=py4j_path,
                          classpath=classpath,
                          javaopts=['-Dfile.encoding=UTF8', '-ea', '-Xmx{}m'.format(max_heap)],
                          die_on_exit=True)

    logging.debug("initializing JVM... ")
    try:
        jvm_gateway = JavaGateway(gateway_parameters=GatewayParameters(port=port, auto_convert=True))
        # # for debugging with Java-side
        # jvm_gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25335, auto_convert=True))
    except Exception as e:
        jvm_gateway = None
        logging.debug("fail")
    logging.debug("success")

    return jvm_gateway.jvm


def get_jvm():
    """현재 생성된 JVM 객체를 반환합니다.

    Returns:
        py4j.java_gateway.JavaGateway: 초기화된 JVM 객체
    """
    global jvm_gateway

    if jvm_gateway is None:
        return None

    return jvm_gateway.jvm
