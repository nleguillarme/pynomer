import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="pynomer",
    version="0.1.1",
    url="https://github.com/nleguillarme/pynomer",
    download_url="https://github.com/nleguillarme/pynomer/archive/0.1.1.tar.gz",
    license="MIT",
    author="nleguillarme",
    author_email="nicolas.leguillarme@univ-grenoble-alpes.fr",
    description="A python wrapper for nomer",
    long_description=read("README.rst"),
    packages=find_packages(exclude=("tests",)),
    install_requires=["setuptools", "requests"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
)
