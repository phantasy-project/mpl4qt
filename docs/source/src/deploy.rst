==========
Deployment
==========

Here're three ways to deploy ``mpl4qt`` to the operating system, although
these approaches are only tested on Linux, hopefully, still work (not tested)
on Windows and Mac OS.

.. _deploy_pre:

Prerequisites
-------------

Required packages: ``Qt5-designer``, ``pyuic5``, ``numpy``, ``matplotlib``.

Normally, all of the Python dependencies will be installed automatically.
Recently, there is one issue regarding starting up Qt designer,
see `here <https://github.com/mu-editor/mu/issues/575>`_,
so it is recommended to use the PyQt5 coming with the OS distribution,
e.g. if you're running Ubuntu/Debian/Linux Mint,
just install the following packages:

.. code-block:: bash

  sudo apt-get update
  sudo apt-get install python3-pyqt5 qttools5-dev-tools pyqt5-dev-tools

Install via PIP
---------------

**Q: How to install pip?**

**A: See `this link <https://pip.pypa.io/en/stable/installing/>`_.**

Install ``mpl4qt``:

.. code-block:: bash

  pip install mpl4qt

Or upgrade from an earlier version by (use ``--no-deps`` if only updating ``mpl4qt``):

.. code-block:: bash

  pip install mpl4qt --upgrade --no-deps

Install from Source
-------------------

Clone the source from Github:

.. code-block:: bash

  git clone https://github.com/archman/python-mpl4qt.git

Then check out to master branch (normally you're already there), and install
into your system by:

.. code-block:: bash

  python3 setup.py install

After Installation
------------------

What could be reached out?
^^^^^^^^^^^^^^^^^^^^^^^^^^
* Command: ``run_designer`` to start Qt5-designer with matplotlib widgets integration.
* Python package named ``mpl4qt`` to be ready for use in any Python script.

Development Environment
^^^^^^^^^^^^^^^^^^^^^^^
* Python: 3.5.2
* matplotlib: 2.2.3
* numpy: 1.14.5
* Qt: 5.5.1
* PyQt: 5.5.1

Qt/PyQt versions could be checked by:

.. code-block:: python

  from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR

  print(QT_VERSION_STR, PYQT_VERSION_STR)

Simple Demo App
^^^^^^^^^^^^^^^

A simple application created with ``mpl4qt`` package could be running by:

.. code-block:: python

    python -m mpl4qt.examples.app1 -c "app1.main()"
