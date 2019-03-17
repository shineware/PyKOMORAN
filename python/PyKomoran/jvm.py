import os
import logging

from py4j.java_gateway import GatewayParameters
from py4j.java_gateway import JavaGateway
from py4j.java_gateway import launch_gateway

jvm_gateway = None


def init_jvm(jar_path="./lib", max_heap=1024):
    base_path = os.path.dirname(os.path.realpath(__file__))
    jar_path = os.path.join(base_path, jar_path)

    assert os.path.exists(jar_path)

    global jvm_gateway

    if jvm_gateway is not None:
        return

    libraries = [
        '{0}{1}KOMORAN-3.3.4.jar',
        '{0}{1}KOMORANEntryPoint-0.1.0.jar',
        '{0}{1}*'
    ]

    classpath = os.pathsep.join([lib.format(jar_path, os.sep) for lib in libraries])
    py4j_path = "{}/py4j0.10.8.1.jar".format(jar_path)

    port = launch_gateway(jarpath=py4j_path,
                          classpath=classpath,
                          javaopts=['-Dfile.encoding=UTF8', '-ea', '-Xmx{}m'.format(max_heap)],
                          die_on_exit=True)

    logging.debug("initializing JVM... ", end="")

    try:
        jvm_gateway = JavaGateway(gateway_parameters=GatewayParameters(port=port, auto_convert=True))
    except Exception as e:
        jvm_gateway = None
        logging.debug("fail")

    logging.debug("success")

    return jvm_gateway.jvm


def get_jvm():
    global jvm_gateway

    if jvm_gateway is None:
        return None

    return jvm_gateway.jvm
