pynomer
=======

.. image:: https://img.shields.io/pypi/v/pynomer.svg
    :target: https://pypi.python.org/pypi/pynomer
    :alt: Latest PyPI version

`pynomer <https://github.com/nleguillarme/pynomer>`_ is a simple python wrapper for `nomer <https://github.com/globalbioticinteractions/nomer>`_.
Nomer is a stand-alone java application which maps identifiers and names to taxonomic names and ontological terms.

Installation
------------

::

  $ pip install pynomer

Usage
-----

As a command-line tool
**********************

::

  pynomer --help
  Usage: pynomer [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      append              Append term match to row using id and name columns...
      clean               Cleans term matcher cache.
      input-schema        Show input schema in JSON.
      matchers            Lists supported matcher and (optionally) their...
      output-schema       Show output schema.
      properties          Lists configuration properties.
      replace             Replace exact term matches in row.
      validate-term       Validate terms.
      validate-term-link  Validate term links.
      version             Show Version.
      
As a python module
**********************

::

    >>> from pynomer import *
    >>> version()
    '0.1.18'

With Docker
**********************

Build image from source:
::

    git clone https://github.com/nleguillarme/pynomer.git
    cd pynomer
    docker build -t pynomer:latest .

Run commands in the container:
::

    docker run -v `pwd`/.nomer:/.nomer pynomer:latest pynomer append "\tHomo sapiens" -e -o json
    
|:warning:| When running pynomer append and replace commands in Docker, you have to use the -e option !

License
-------

License: MIT

Authors
-------

`pynomer` was written by `nleguillarme <nicolas.leguillarme@univ-grenoble-alpes.fr>`_.
