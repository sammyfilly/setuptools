==================================================
Building and Distributing Packages with Setuptools
==================================================

The first step towards sharing a Python library or program is to build a
distribution package [#package-overload]_. This includes adding a set of
additional files containing metadata and configuration to not only instruct
``setuptools`` on how the distribution should be built but also
to help installer (such as :pypi:`pip`) during the installation process.

This document contains information to help Python developers through this
process. Please check the :doc:`/userguide/quickstart` for an overview of
the workflow.

Also note that ``setuptools`` is what is known in the community as :pep:`build
backend <517#terminology-and-goals>`, user facing interfaces are provided by tools
such as :pypi:`pip` and :pypi:`build`. To use ``setuptools``, one must
explicitly create a ``pyproject.toml`` file as described :doc:`/build_meta`.


Contents
========

.. toctree::
    :maxdepth: 1

    quickstart
    package_discovery
    dependency_management
    development_mode
    entry_point
    datafiles
    ext_modules
    distribution
    miscellaneous
    extension
    declarative_config
    pyproject_config

---

.. rubric:: Notes

.. [#package-overload]
   A :term:`Distribution Package` is also referred in the Python community simply as "package"
   Unfortunately, this jargon might be a bit confusing for new users because the term package
   can also to refer any :term:`directory <package>` (or sub directory) used to organize
   :term:`modules <module>` and auxiliary files.
Documentation#
Setuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects.

It helps developers to easily share reusable code (in the form of a library) and programs (e.g., CLI/GUI tools implemented in Python), that can be installed with pip and uploaded to PyPI.

For Enterprise
 Tidelift
Professional support for setuptools is available as part of the Tidelift Subscription. Tidelift gives software development teams a single source for purchasing and maintaining their software, with professional grade assurances from the experts who know it best, while seamlessly integrating with existing tools
