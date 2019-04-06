설치하기
=======================================

이 문서에서는 Python에서 KOMORAN을 사용하기 위해 PyKOMORAN을 설치하는 방법을 살펴보도록 하겠습니다.

.. Note::
   PyKOMORAN은 KOMORAN을 Python에서 사용할 수 있도록 하는 프로젝트입니다.
   이는 KOMORAN을 Python으로 재작성한 것이 아니라, Python에서 Java용 KOMORAN을 실행하는 것을 뜻합니다.

.. Note::
   문서의 내용 중 지원되지 않거나 잘못된 내용을 발견하실 경우,
   `PyKOMORAN 프로젝트에 이슈 <https://github.com/shineware/PyKOMORAN/issues>`_ 를 남겨주세요.

----

환경 준비
---------------------------------------

Java
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
KOMORAN을 실행하기 위한 Java 환경이 준비되어야 합니다.
Java 8 이상의 버전을 사용하셔야 하며, 사용하고 계신 Java 버전은 다음과 같이 확인하실 수 있습니다. ::

   java -version

아직 Java 환경이 설치되어 있지 않다면, 다음 링크 중 하나를 이용하여 Java 환경을 설치하실 수 있습니다.

* `OpenJDK 설치하기 <https://openjdk.java.net/install/>`_
* `Oracle Java 설치하기 <https://www.oracle.com/technetwork/java/javase/downloads/index.html>`_

.. Note::
   Java 환경의 설치가 익숙하지 않으시다면, `검색엔진에서 설치 방법을 검색 <https://www.google.com/search?q=jdk+설치>`_
   해보시는 것을 권장합니다.

.. Note::
   OpenJDK에서의 동작 중 별다른 문제점은 아직 알려지지 않았습니다.
   OpenJDK 사용 중 이슈가 발생한다면 `알려주시기를 <https://github.com/shineware/PyKOMORAN/issues>`_ 부탁드립니다.

Python 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PyKOMORAN은 Python 3.4 이상을 지원합니다. 사용하고 계신 Python 버전은 다음과 같이 확인하실 수 있습니다. ::

  python --version
  # 또는, python3 버전을 확인해보실 수 있습니다.
  python3 --version

또는, `Python 홈페이지 <https://www.python.org/downloads/>`_ 에서 최신 버전의 Python을 설치하실 수 있습니다.

.. Note::
    Python 2.7은 2019년 12월 31일을 마지막으로 지원이 종료될 예정으로,
    PyKOMORAN은 Python 2.7을 지원하지 않도록 개발되었습니다.

Py4J
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`Py4J <https://www.py4j.org/>`_ 는 Java 버전의 KOMORAN을 Python에서 실행할 수 있도록 도와주는 Library입니다.
아래 `pip 패키지 관리도구`_ 를 이용하여 PyKomoran을 설치하는 경우 **자동으로 함께 설치** 됩니다.

pip 패키지 관리도구
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PyKOMORAN은 PyPI(Python Package Index)를 통해 설치하시는 것이 가장 편하고 쉽습니다.
이를 위해 Python 3.4 이상을 지원하는 pip가 설치되어있는지 다음과 같이 확인하실 수 있습니다. ::

  pip --version
  # 또는, pip3 버전을 확인해보실 수 있습니다.
  pip3 --version

위 명령어는 pip 버전과 함께 Python 버전을 출력합니다.


설치하기
---------------------------------------
`pip 패키지 관리도구`_ 를 이용하는 경우 다음의 명령어를 실행하여 설치하실 수 있습니다. ::

  pip install PyKomoran


소스코드 다운로드
---------------------------------------
PyKOMORAN를 분석하시거나, 기여를 위해 소스코드를 직접 다운로드 받으실 수도 있습니다.
꾸준한 업그레이드를 위해 Git 도구를 이용하여 GitHub 저장소에서 복제받는 방법을 권장합니다. ::

   git clone https://github.com/shineware/PyKOMORAN

다운로드 후에는 해당 디렉토리 내에서 `git pull` 명령어를 통해 최신 소스를 받아올 수 있습니다. ::

   cd PyKOMORAN
   git pull

.. seealso::
  Git 도구 홈페이지에서 `사용법 <https://git-scm.com/book/ko/>`_ 을 익히실 수 있습니다.

.. Note::
  특정 버전의 PyKOMORAN을 다운로드 받으실 때는 `GitHub 저장소의 배포 메뉴 <https://github.com/shineware/PyKOMORAN/releases>`_
  를 이용하시면 버전별로 압축된 소스코드를 다운로드 받으실 수 있습니다.
