"""
PyNomer is a simple python wrapper for nomer
"""
from setuptools import find_packages, setup

dependencies = ["click", "setuptools", "requests"]

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pynomer",
    version="v0.1.2",
    url="https://github.com/nleguillarme/pynomer",
    license="MIT",
    author="Nicolas Le Guillarme",
    author_email="nicolas.leguillarme@univ-grenoble-alpes.fr",
    description="A python wrapper for nomer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=dependencies,
    entry_points={"console_scripts": ["pynomer = pynomer.cli:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
)
