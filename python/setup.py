import os
import sys
from setuptools import setup
from setuptools import find_packages
from distutils.util import convert_path

version_properties = dict()
version_filename = convert_path(os.path.join('PyKomoran', '__version__.py'))
with open(version_filename) as version_file:
    exec(version_file.read(), version_properties)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_requires = [
]

install_requires = [
    'py4j==0.10.8.1',
]

tests_require = [
    'coverage==4.5.3',
    'nose==1.3.7',
]

# if sys.version_info < (2, 7):
#     tests_require.append('unittest2==0.5.1')

dependency_links = [
]
# @formatter:off
setup(
    name                            = version_properties['__title__'],
    version                         = version_properties['__version__'],
    description                     = version_properties['__description__'],
    url                             = version_properties['__url__'],
    author                          = version_properties['__author__'],
    author_email                    = version_properties['__author_email__'],
    maintainer                      = version_properties['__author__'],
    maintainer_email                = version_properties['__author_email__'],
    contact                         = version_properties['__author__'],
    contact_email                   = version_properties['__author_email__'],
    license                         = version_properties['__license__'],
    classifiers                     = [
                                        "Development Status :: 4 - Beta",
                                        "Environment :: Console",
                                        "Intended Audience :: Developers",
                                        "Intended Audience :: Education",
                                        "Intended Audience :: Information Technology",
                                        "Intended Audience :: Science/Research",
                                        "License :: OSI Approved :: Apache Software License",
                                        "Natural Language :: Korean",
                                        "Programming Language :: Java",
                                        "Programming Language :: Python :: 3 :: Only",
                                        "Programming Language :: Python :: 3.4",
                                        "Programming Language :: Python :: 3.5",
                                        "Programming Language :: Python :: 3.6",
                                        "Programming Language :: Python :: 3.7",
                                        "Topic :: Scientific/Engineering :: Information Analysis",
                                        "Topic :: Software Development :: Libraries :: Java Libraries",
                                        "Topic :: Text Processing :: Linguistic"
                                    ],
    keywords                        = [
                                        'KOMORAN', 'KOrean MORphical ANalyzer',
                                        'MORphical Analyzer', 'Text Analyzer',
                                        'Tokenizer', 'PoS Tagger',
                                        'Korean', 'Linguistic', 'NLP',
                                        'Natural Language Processing',
                                    ],
    download_url                    = version_properties['__download_url__'],
    include_package_data            = True,
    long_description                = long_description,
    long_description_content_type   = 'text/markdown',
    packages                        = find_packages(),
    install_requires                = install_requires,
    setup_requires                  = setup_requires,
    tests_require                   = tests_require,
    extras_require                  = {
                                        'test': tests_require,
                                    },
    dependency_links                = dependency_links,
    test_suite                      = 'nose.collector',
)
# @formatter:on
