# PyKOMORAN

[![DOI](https://zenodo.org/badge/175813952.svg)](https://zenodo.org/badge/latestdoi/175813952)

## Introduction

* PyKOMORAN is Python wrapper project for [KOMORAN, KOrean MORphical ANalyzer](https://github.com/shin285/KOMORAN).
* PyKOMORAN is using [Py4J](https://github.com/bartdag/py4j) for wrapping [KOMORAN Java library](https://github.com/shin285/KOMORAN).
* If you have any issue or question, please leave an issue on [PyKOMORAN Project](https://github.com/shineware/PyKOMORAN/issues).

## Installation

### Requirements

* To use PyKomoran, the following requirements must be installed
  * Java 8+ JDK Environment
  * Python 3
    * We recommend you use Python 3.4 or higher.
  * [Py4J](https://www.py4j.org/install.html), 0.10 (or higher)
    * This will be installed when installing PyKomoran using `pip`.

### How to install

* You can install PyKomoran using `pip`.

```bash
  pip install PyKomoran
```

* Or, just clone this repository and copy for use.

```bash
  git clone https://github.com/shineware/PyKOMORAN
  cp -r PyKOMORAN/python/PyKomoran [DEST_LOCATION_TO_YOUR_PROJECT]
```

* Please refer to [installation document](https://docs.komoran.kr/pykomoran/installation.html?utm_source=GitHub&utm_medium=Referral&utm_campaign=PyKomoran) for detailed installation method.

## Usage

### Quick start

* After import dependencies, create a Komoran instance.

```python
  from PyKomoran import *
  komoran = Komoran()
```

* After then, run analyzing method.

```python
  komoran.get_plain_text("① 대한민국은 민주공화국이다.")
  # # Result
  # ①/SW 대한민국/NNP 은/JX 민주공화국/NNP 이/VCP 다/EF ./SF
```

### Usage in detail

* Please refer [KOMORAN Document site](https://docs.komoran.kr/pykomoran/tutorial.html?utm_source=GitHub&utm_medium=Referral&utm_campaign=PyKomoran) for more information.

## Citation

* PyKOMORAN provide DOI(Digital Object Identifier) using [Zenodo](https://zenodo.org).
* Please refer below links when citing PyKOMORAN.
  * [DOI JSON Export](https://zenodo.org/record/2619178/export/json)
  * [DOI BibTeX Export](https://zenodo.org/record/2619178/export/hx)

## License

* PyKOMORAN is distributed with the Apache 2.0 license, same as [KOMORAN](https://github.com/shin285/KOMORAN). See `LICENSE` for more information.

## Contributing

* We're always happy to receive any contributions including code, bug reports and documentation fixes.
* Please visit our [Website](https://www.shineware.co.kr/products/komoran/#demo?utm_source=GitHub&utm_medium=Referral&utm_campaign=PyKomoran) and/or [Project Organization at GitHub](https://github.com/komoran) for more information.
* Or, if you have any necessary features or suggestion? Please leave your idea on [Request to add new feature](https://github.com/shineware/PyKOMORAN/issues/new?template=FEATURE_REQUEST.md)
