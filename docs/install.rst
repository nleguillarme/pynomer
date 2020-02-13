Installing pynomer
************************

Download and build nomer-docker container
=========================================

pynomer uses HTTP requests to access nomer commands exposes by a dockerized RESTful API.

Download nomer-docker image from GitHub (https://github.com/nleguillarme/nomer-docker)
and build the container using the following command.

.. code-block:: bash

  docker build -t nomer-docker:latest .

Install pynomer python package
==============================

pynomer stable version can be installed from PyPi.

::

  pip install pynomer
