Installing pynomer
************************

Download and build nomer-docker container
=========================================

pynomer uses Docker to run nomer. The container is built as follows:

.. code-block:: bash

  docker build github.com/nleguillarme/nomer-docker#master:docker -t nomer-docker

Install pynomer python package
==============================

pynomer stable version can be installed from PyPi.

::

  pip install pynomer
