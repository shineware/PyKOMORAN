# PyKOMORAN

[한국어](README.md) | [English](README.en.md)

## 소개

* PyKOMORAN은 Python에서 한국어 형태소 분석기인 [KOMORAN](https://github.com/shin285/KOMORAN)을 사용할 수 있도록 하는 프로젝트입니다.
* PyKOMORAN은 [Py4J](https://github.com/bartdag/py4j)를 이용하여 [KOMORAN Java Library](https://github.com/shin285/KOMORAN)를 실행합니다.
* 사용 중 이슈나 질문이 있다면 [PyKOMORAN 프로젝트](https://github.com/komoran/PyKOMORAN/issues)에 이슈를 남겨주세요.

## 설치

### 필요사항

* PyKomoran을 이용하기 위해서는 다음의 요구사항이 설치되어 있어야 합니다.
  * Java 8 이상의 JDK 환경
  * [Py4J](https://www.py4j.org/install.html), 0.10.8 이상
    * `pip`를 이용하여 간편하게 설치(`pip install py4j`)하는 것을 권장합니다.
  * Python 3 이상
    * Python 3.6 이상을 사용하는 것을 권장합니다.

### 설치방법

* `pip`를 이용하여 PyKomoran을 설치할 수 있습니다.

  ```sh
    pip install PyKomoran
  ```

* 또는, 소스코드를 다운로드받아 설치할 수 있습니다.

  ```sh
    git clone https://github.com/komoran/PyKOMORAN
    cp -r PyKOMORAN/python/PyKomoran [사용하실 PROJECT 위치]
  ```

## 사용법

### 빠른 사용 방법

* 의존성을 불러온 후, KOMORAN 객체를 만듭니다.

  ```python
    from PyKomoran import *
    komoran = Komoran()
  ```

* 분석 메소드를 이용하여 문장을 분석합니다.

  ```python
    komoran.get_plain_text("① 대한민국은 민주공화국이다.")
    # # 실행 결과
    # ①/SW 대한민국/NNP 은/JX 민주공화국/NNP 이/VCP 다/EF ./SF
  ```

### 자세한 사용법

* 자세한 사용방법은 [KOMORAN 문서 사이트](https://docs.komoran.kr)을 확인해주시기 바랍니다.

## 라이선스

* PyKOMORAN은 KOMORAN과 동일한 Apache 2.0 라이선스로 배포됩니다.
* 자세한 내용은 [LICENSE](LICENSE) 파일을 참고해주시기 바랍니다.

## 기여하기

* 소스 코드나 버그 리포트, 문서 내의 오타 수정 등 어떠한 기여도 환영합니다.
* [Komoran Website](https://www.shineware.co.kr/products/komoran/#demo?utm_source=komoran-kr&utm_medium=Referral&utm_campaign=github-PyKomoran) 또는 [KOMORAN GitHub 페이지](https://github.com/komoran)를 참고해주세요!
* 또는, 필요한 기능이나 제안이 있으신가요? [기능 추가 요청](https://github.com/komoran/PyKOMORAN/issues/new?template=FEATURE_REQUEST.md)을 남겨주세요!
