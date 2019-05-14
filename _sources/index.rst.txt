PyKOMORAN 문서
=======================================

PyKOMORAN은 Java로 개발된 형태소 분석기인 `KOMORAN <https://www.shineware.co.kr/products/komoran/>`_ [#f1]_ 을 Python에서도 사용 가능하도록 개발한 것입니다.

.. Note::
   PyKOMORAN은 KOMORAN과 동일한 `Apache 2.0 License <https://www.apache.org/licenses/LICENSE-2.0>`_ 로 배포되고 있습니다.
   이는 누구나 자유롭게 다운로드 받아 부분 또는 전체를 개인적 또는 상업적 목적으로 이용할 수 있음을 뜻합니다.
   더 자세한 내용은 `Apache License <https://www.apache.org/licenses/>`_ 를 참고해주세요.

----

참고자료
---------------------------------------

PyKOMORAN 참고 자료
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
KOMORAN을 개발한 SHINEWARE에서 제공하는 참고자료입니다.

* `PyKOMORAN 저장소 <https://github.com/shineware/PyKOMORAN>`_ 에 전체 소스 코드가 공개되어 있습니다.
* `PyPI 저장소 <https://pypi.org/project/PyKomoran/>`_ 에서 바로 설치 가능한 패키지를 확인하실 수 있습니다.
* :doc:`/firststep/installation` 에서 설치 방법을 확인해보세요.
* 사용 중 문제나 궁금증이 있으시다면 `저장소의 이슈 메뉴 <https://github.com/shineware/PyKOMORAN/issues>`_ 에 남겨주세요.
* `KOMORAN Slack <https://komoran.slack.com/join/shared_invite/MTc3NTMzMDQ1NTY5LTE0OTM4MjE5MzktNDE3NmQ4NDNkNw>`_ 에 방문하셔서 사용법과 팁 등을 공유해주세요.

다른 언어에서의 KOMORAN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Java과 R에서 KOMORAN을 사용할 수 있습니다.

* Java에서 사용 가능한 KOMORAN
   * PyKOMORAN이 참고하고 있는 형태소 분석기 프로젝트입니다.
   * `GitHub 저장소 <https://github.com/shin285/KOMORAN>`_ 에 바로 실행할 수 있는 소스 코드가 공개되어 있습니다.
   * `SHINEWARE 홈페이지 <https://shineware.co.kr>`_ 에서 `KOMORAN 소개 및 데모 <https://www.shineware.co.kr/products/komoran/>`_ 를 확인하실 수 있습니다.
* R에서 사용 가능한 RKOMORAN (*개발 중*)
   * `RKOMORAN 저장소 <https://github.com/shineware/RKOMORAN>`_ 에 *현재 개발 중인* 소스 코드가 공개되어 있습니다.

그 외 참고 자료
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
사용자 분들께서 만들어주신 참고자료입니다.

* `Junghwan Park <https://github.com/9bow>`_ 님께서 Java로 개발한 `Simple API Server <https://github.com/9bow/KOMORANRestAPIServer>`_ 를 사용해보실 수 있습니다.
* `Hyunjoong Kim <https://github.com/lovit>`_ 님께서 Python으로 개발한 `KOMORAN3Py <https://github.com/lovit/komoran3py>`_ 도 공개되어 있습니다.


분석 예시
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* 아래는 `KOMORAN 데모 <https://www.shineware.co.kr/products/komoran/>`_ 를 이용한 분석 예시입니다.
* 입력 문장: `대한민국은 민주공화국이다.`

.. image:: _static/images/KOMORAN_Sample_01.png
   :width: 640 px
   :alt: KOMORAN 분석 예시 #1
   :align: center

* 입력 문장: `대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.`

.. image:: _static/images/KOMORAN_Sample_02.png
   :width: 640 px
   :alt: KOMORAN 분석 예시 #2
   :align: center


.. toctree::
   :maxdepth: 2
   :caption: PyKOMORAN 첫걸음
   :name: firststep

   /firststep/installation
   /firststep/tutorial
   /firststep/postypes


.. toctree::
   :maxdepth: 2
   :caption: PyKOMORAN 사용하기
   :name: usage

   /usage/default-models


.. toctree::
   :maxdepth: 2
   :caption: API 소개
   :name: api

   /api/python/modules
   /api/java/packages



.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`


.. [#f1]
   한국어 형태소 분석기를 뜻하는 KOrean MORphical ANalyzer의 약자입니다.
