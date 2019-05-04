3줄의 코드로 형태소 분석 시작하기
===========================================================

이 문서에서는 PyKOMORAN을 이용하여 3줄의 Python 코드 만으로 간단한 형태소 분석을 해보도록 하겠습니다.
아직 PyKOMORAN을 설치하지 않으셨다면, 먼저 :doc:`installation` 문서를 참고해주세요.

.. Note::
   문서의 내용 중 지원되지 않거나 잘못된 내용을 발견하실 경우,
   `PyKOMORAN 프로젝트에 이슈 <https://github.com/shineware/PyKOMORAN/issues>`_ 를 남겨주세요.

----

전체 코드 보기
---------------------------------------
이번 튜토리얼에서 사용할 전체 코드는 다음과 같습니다. (딱 3줄입니다!)

.. code-block:: python
  :linenos:

  from PyKomoran import *
  komoran = Komoran("EXP")
  print(komoran.get_plain_text("KOMORAN은 한국어 형태소 분석기입니다."))

실행 결과는 다음과 같습니다.

.. code-block:: python

  # KOMORAN/SL 은/JX 한국어/NNP 형태소/NNP 분석기/NNG 이/VCP ㅂ니다/EF ./SF

이제, 위 코드를 한줄씩 살펴보도록 하겠습니다.

PyKomoran 불러오기
---------------------------------------
Python 명령어를 실행한 후, 다음과 같이 PyKomoran을 불러옵니다.

.. code-block:: python
  :linenos:

  from PyKomoran import *

위 명령어는 PyKomoran 패키지에 포함된 모든 모듈을 불러옵니다.


Komoran 객체 생성하기
---------------------------------------
이제, 형태소 분석을 위한 ``Komoran`` 객체를 생성합니다.
여기에서는 기본으로 제공하는 모델 중 FULL 모델을 불러오겠습니다.

.. code-block:: python
  :linenos:

  komoran = Komoran("EXP")

이 과정에서 Java 버전의 KOMORAN을 불러오게 되며, 약간의 시간이 소요됩니다.
이제 ``Komoran`` 객체의 메소드를 이용하여 형태소를 분석할 수 있습니다.

.. Note::
  ``DEFAULT_MODEL`` 은 기본적으로 PyKomoran에 포함된 모델로, KOMORAN의 ``DEFAULT_MODEL`` 에 대응합니다.
  즉, PyKOMORAN의 ``"EXP"`` 과 ``"STABLE"`` 은 각각 KOMORAN의 ``DEFAULT_MODEL.FULL`` 과
  ``DEFAULT_MODEL.LIGHT`` 에 대응합니다.

.. TODO::
  DFEAULT_MODEL에 대한 설명을 추가합니다.

형태소 분석하기
---------------------------------------
PyKOMORAN은 KOMORAN에서 제공하는 다양한 형태의 형태소 분석 결과를 제공합니다.
우선 입력 문장을 형태소 별로 나누어 ``형태소/품사`` 형태로 태깅된 결과를 보도록 하겠습니다.

.. code-block:: python
  :linenos:

  print(komoran.get_plain_text("KOMORAN은 한국어 형태소 분석기입니다."))

  # # 실행 결과
  # KOMORAN/SL 은/JX 한국어/NNP 형태소/NNP 분석기/NNG 이/VCP ㅂ니다/EF ./SF

형태소 분석의 결과인 품사 기호는 :doc:`/firststep/postypes` 에서 찾아보실 수 있습니다.

다양한 방법으로 형태소 분석하기
---------------------------------------
위에서 살펴본 ``get_plain_text()`` 메소드 외에도, 다양한 메소드들을 지원합니다.
(:doc:`/api/python/PyKomoran.core` 참고)

.. code-block:: python
  :linenos:

  # PyKomoran 불러오기
  from PyKomoran import *

  # Komoran 객체 생성
  komoran = Komoran("EXP")

  # 분석할 문장 준비
  str_to_analyze = "① 대한민국은 민주공화국이다. ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."

  # get_nouns(): 입력 문장에서 명사만 추출합니다.
  print(komoran.get_nouns(str_to_analyze))
  # # 실행 결과
  # ['대한민국', '민주공화국', '대한민국', '주권', '국민', '권력', '국민']

  # get_morphes_by_tags(): 입력 문장에서 주어진 품사들만 추출합니다.
  print(komoran.get_morphes_by_tags(str_to_analyze, tag_list=['NNP', 'NNG', 'SF']))
  # # 실행 결과
  # ['대한민국', '민주공화국', '.', '대한민국', '주권', '국민', '권력', '국민', '.']

  # get_plain_text(): 입력 문장 내에 형태소/품사 형태로 태그를 합니다.
  print(komoran.get_plain_text(str_to_analyze))
  # # 실행 결과
  # ①/SW 대한민국/NNP 은/JX 민주공화국/NNP 이/VCP 다/EF ./SF ②/SW 대한민국/NNP 의/JKG 주권/NNP 은/JX 국민/NNG 에게/JKB 있/VV 고/EC ,/SP 모든/MM 권력/NNG 은/JX 국민/NNG 으로부터/JKB 나오/VV ㄴ다/EF ./SF

  # get_token_list(): 입력 문장에 대해서 형태소/품사/시작지점/종료지점을 갖는 Token 자료형들을 반환받습니다.
  print(komoran.get_token_list(str_to_analyze))
  # # 실행 결과
  # [①/SW(0,1), 대한민국/NNP(2,6), 은/JX(6,7), 민주공화국/NNP(8,13), 이/VCP(13,14), 다/EF(14,15), ./SF(15,16), ②/SW(17,18), 대한민국/NNP(19,23), 의/JKG(23,24), 주권/NNP(25,27), 은/JX(27,28), 국민/NNG(29,31), 에게/JKB(31,33), 있/VV(34,35), 고/EC(35,36), ,/SP(36,37), 모든/MM(38,40), 권력/NNG(41,43), 은/JX(43,44), 국민/NNG(45,47), 으로부터/JKB(47,51), 나오/VV(52,54), ㄴ다/EF(53,55), ./SF(55,56)]

  # get_token_list(flatten=False): 입력 문장에 대해서 Token 자료형들을 반환받습니다. 이 때, 어절 단위로 나누어 반환받습니다.
  print(komoran.get_token_list(str_to_analyze, flatten=False))
  # # 실행 결과
  # [[①/SW(0,1)], [대한민국/NNP(2,6), 은/JX(6,7)], [민주공화국/NNP(8,13), 이/VCP(13,14), 다/EF(14,15), ./SF(15,16)], [②/SW(17,18)], [대한민국/NNP(19,23), 의/JKG(23,24)], [주권/NNP(25,27), 은/JX(27,28)], [국민/NNG(29,31), 에게/JKB(31,33)], [있/VV(34,35), 고/EC(35,36), ,/SP(36,37)], [모든/MM(38,40)], [권력/NNG(41,43), 은/JX(43,44)], [국민/NNG(45,47), 으로부터/JKB(47,51)], [나오/VV(52,54), ㄴ다/EF(53,55), ./SF(55,56)]]

  # get_token_list(flatten=False): 입력 문장에 대해서 Token 자료형들을 반환받습니다. 이 때, 품사 기호 대신 이름을 사용합니다.
  print(komoran.get_token_list(str_to_analyze, use_pos_name=True))
  # # 실행 결과
  # [①/기타기호(논리수학기호,화폐기호)(0,1), 대한민국/고유 명사(2,6), 은/보조사(6,7), 민주공화국/고유 명사(8,13), 이/긍정 지정사(13,14), 다/종결 어미(14,15), ./마침표,물음표,느낌표(15,16), ②/기타기호(논리수학기호,화폐기호)(17,18), 대한민국/고유 명사(19,23), 의/관형격 조사(23,24), 주권/고유 명사(25,27), 은/보조사(27,28), 국민/일반 명사(29,31), 에게/부사격 조사(31,33), 있/동사(34,35), 고/연결 어미(35,36), ,/쉼표,가운뎃점,콜론,빗금(36,37), 모든/관형사(38,40), 권력/일반 명사(41,43), 은/보조사(43,44), 국민/일반 명사(45,47), 으로부터/부사격 조사(47,51), 나오/동사(52,54), ㄴ다/종결 어미(53,55), ./마침표,물음표,느낌표(55,56)]

  # get_list(): 입력 문장에 대해서 형태소/품사를 갖는 Pair 자료형들을 반환받습니다.
  print(komoran.get_list(str_to_analyze))
  # # 실행 결과
  # [①/SW, 대한민국/NNP, 은/JX, 민주공화국/NNP, 이/VCP, 다/EF, ./SF, ②/SW, 대한민국/NNP, 의/JKG, 주권/NNP, 은/JX, 국민/NNG, 에게/JKB, 있/VV, 고/EC, ,/SP, 모든/MM, 권력/NNG, 은/JX, 국민/NNG, 으로부터/JKB, 나오/VV, ㄴ다/EF, ./SF]


위에서 사용한 메소드들에 대한 자세한 설명은 API 문서 :doc:`/api/python/PyKomoran.core` 를 참고해주세요.

결론
---------------------------------------
지금까지 Python에서 PyKomoran을 이용하여 형태소 분석을 하는 간단한 예제를 살펴보았습니다.

위 예제 코드는 `PyKOMORAN tutorials 저장소 <https://github.com/shineware/tutorials/blob/master/PyKOMORAN>`_ 에서 확인하시거나, 아래에서 링크에서 다운로드 받으실 수 있습니다.

* `3줄의 코드로 형태소 분석 시작하기 예제 코드 다운로드 (.py) <https://github.com/shineware/tutorials/blob/master/PyKOMORAN/bootstrap/bootstrap.py>`_
* `3줄의 코드로 형태소 분석 시작하기 예제 코드 다운로드 (.ipynb) <https://github.com/shineware/tutorials/blob/master/PyKOMORAN/bootstrap/bootstrap.ipynb>`_
