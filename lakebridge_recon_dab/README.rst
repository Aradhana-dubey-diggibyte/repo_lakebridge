========
Overview
========


.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/lakebridge_recon_dab/badge/?style=flat
    :target: https://readthedocs.org/projects/lakebridge_recon_dab/
    :alt: Documentation Status
.. |github-actions| image:: https://github.com/ionelmc/lakebridge_recon_dab/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/lakebridge_recon_dab/actions
.. |codecov| image:: https://codecov.io/gh/ionelmc/lakebridge_recon_dab/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/ionelmc/lakebridge_recon_dab
.. |version| image:: https://img.shields.io/pypi/v/lakebridge-recon-dab.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/lakebridge-recon-dab
.. |wheel| image:: https://img.shields.io/pypi/wheel/lakebridge-recon-dab.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/lakebridge-recon-dab
.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/lakebridge-recon-dab.svg
    :alt: Supported versions
    :target: https://pypi.org/project/lakebridge-recon-dab
.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/lakebridge-recon-dab.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/lakebridge-recon-dab
.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/lakebridge_recon_dab/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/lakebridge_recon_dab/compare/v0.0.0...main


An example package. Generated with cookiecutter-pylibrary.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install lakebridge-recon-dab

You can also install the in-development version with::

    pip install https://github.com/ionelmc/lakebridge_recon_dab/archive/main.zip


Documentation
=============


https://lakebridge_recon_dab.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
