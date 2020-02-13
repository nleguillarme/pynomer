pynomer
=======

.. image:: https://img.shields.io/pypi/v/pynomer.svg
    :target: https://pypi.python.org/pypi/pynomer
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status
   
.. image:: https://readthedocs.org/projects/pynomer/badge/?version=latest
    :target: https://pynomer.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

`pynomer <https://github.com/nleguillarme/pynomer>`_ is a simple python wrapper for `nomer <https://github.com/globalbioticinteractions/nomer>`_.
Nomer is a stand-alone java application which maps identifiers and names to taxonomic names and ontological terms.

Usage
-----

See full documentation at https://pynomer.readthedocs.io/en/latest/.

Installation
------------

Download and build nomer-docker container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

pynomer uses Docker to run nomer. The container is built as follows:

.. code-block:: bash

  docker build github.com/nleguillarme/nomer-docker#master:docker -t nomer-docker

Install pynomer python package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

pynomer stable version can be installed from PyPi.

::

  pip install pynomer


License
-------

License: MIT

Authors
-------

`pynomer` was written by `nleguillarme <nicolas.leguillarme@univ-grenoble-alpes.fr>`_.
