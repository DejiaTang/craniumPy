.. _start here: 

Start Here
===========

.. _right for you:

Is Cranium right for you? 
+++++++++++++++++++++++++++

Cranium may be able to help you if:

- your data consists of a set of 3D image stacks
- your data contains a clear structure and shape that has consistent gross morphology between control and experimental samples
- you want to identify extreme or subtle differences in the structure between your experimental groups
- you want to compare up to 4 different image channels

Cranium cannot help if:

- your data was collected using cryosections that need to be aligned after imaging
- your experimental changes the gross morphology of the sample between control and experimental samples

.. _install:

Installation
+++++++++++++

Cranium is most easily installed using `pip`_, Python's package installer. However, Cranium's dependencies can be difficult to install using pip, so we recommend that you install `Anaconda`_ to manage more complicated packages. See `Setting up a Python environment <python set up>`_ for more details. 

.. code::
	
	$ pip install cranium

.. note:: If you are unfamiliar with the command line, check out `this tutorial <command line tutorial>`_. Additional resources regarding the command line are available `here <resources>`_.

.. warning:: Packages required for cranium depend on Visual C++ Build Tools, which can be downloaded `here <Build Tools>`_.

.. _python set up:

Setting up a Python environment
++++++++++++++++++++++++++++++++

If you're new to scientific computing with Python, we recommend that you install `Anaconda`_ to manage your Python installation. Anaconda is a framework for scientific computing with Python that will install important packages (`numpy`_, `scipy`_, and `matplotlib`_) that cannot be easily installed with `pip`_, which is the build in Python package installer.

.. warning:: Cranium is written in Python 3, so we recommend that you install the Python 3 version of Anaconda. 

.. _Anaconda: https://www.anaconda.com/what-is-anaconda/
.. _pip: https://en.wikipedia.org/wiki/Pip_(package_manager)
.. _numpy: http://www.numpy.org/
.. _scipy: https://www.scipy.org/
.. _matplotlib: https://matplotlib.org/
.. _command line tutorial: http://www.vikingcodeschool.com/web-development-basics/a-command-line-crash-course
.. _pip tutorial: https://programminghistorian.org/lessons/installing-python-modules-pip
.. _Build Tools: http://landinghub.visualstudio.com/visual-cpp-build-tools