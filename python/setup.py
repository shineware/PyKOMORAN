import os
import sys
from setuptools import setup
from setuptools import find_packages
from distutils.util import convert_path

version_properties = dict()
version_filename = convert_path(os.path.join('PyKomoran', '__version__.py'))
with open(version_filename) as version_file:
    exec(version_file.read(), version_properties)

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
    name                    = version_properties['__title__'],
    version                 = version_properties['__version__'],
    description             = version_properties['__description__'],
    url                     = version_properties['__url__'],
    author                  = version_properties['__author__'],
    author_email            = version_properties['__author_email__'],
    maintainer              = version_properties['__author__'],
    maintainer_email        = version_properties['__author_email__'],
    contact                 = version_properties['__author__'],
    contact_email           = version_properties['__author_email__'],
    license                 = version_properties['__license__'],
    classifiers             = version_properties['__classifiers__'],
    download_url            = version_properties['__download_url__'],
    packages                = find_packages(),
    install_requires        = install_requires,
    setup_requires          = setup_requires,
    tests_require           = tests_require,
    extras_require          = {
                                'test': tests_require,
                            },
    dependency_links        = dependency_links,
    test_suite              = 'nose.collector',
    # scripts=['manage.py'],
    # entry_points={
    #     'console_scripts': [
    #     ],
    # },
)
# @formatter:on
