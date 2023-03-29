# Author: Yuichi Shindo <chiru9.shindou@gmail.com>
# Copyright (c) 2023 Yuichi Shindo
# License: MIT MIT License

from setuptools import setup
import algomath_def

DESCRIPTION = "algomath_def:Libraries of each major function for algorithmic understanding,and for learning Github and learning Python "
NAME = 'algomath_def'
AUTHOR = 'Yuichi Shindo'
AUTHOR_EMAIL = 'chiru9.shindou@gmail.com'
URL = 'https://github.com/yuichi-shindo/test'
LICENSE = 'MIT Licence'
DOWNLOAD_URL = 'https://github.com/yuichi-shindo/test'
VERSION = algomath_def.__version__
PYTHON_REQUIRES = ">=3.6"

#このライブラリを使うのに必要な別のライブラリを記載する、記載方法は以下
INSTALL_REQUIRES = [
 
]

EXTRAS_REQUIRE = {

}

PACKAGES = [
    'algomath_def'
]

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
]

with open('README.md', 'r') as fp:
    readme = fp.read()

LONG_DESCRIPTION = readme 

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
    )