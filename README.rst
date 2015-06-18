================================
``pageup init`` ``pageup build``
================================
``pageup`` is a little python tool used to automate the upkeep of my book
club and a few other single page static sites.

Made with `jinja2`_ and `docutils`_.

.. _jinja2: http://jinja.pocoo.org/
.. _docutils: http://docutils.sourceforge.net/


Usage
-----
``pageup`` is pretty simple. 

================  ===============================================================
Command           Description
================  ===============================================================
``pageup``        Prints help menu.
``pageup build``  Generates the page (index.html)
``pageup init``   Populates current working directory with necessary files
``pageup init mysite``  Creates ``mysite`` directory and populates that with necessary files.
================  ===============================================================

Necessary files are ``content.rst``, ``style.css``, and ``template.jinja``.
These are templates for you to modify.


Installation:
-------------

.. code::

    $ pip install git+https://github.com/ElijahCaine/pageup.git


Setup
-----
Here's what your directory structure should look like

.. code::

    yourdomain.bla/
        somepage/
            content.rst
            style.css
            template.jinja
            index.html      # This file is generated with `pageup build` 

``somepage`` depends on whatever you want ``yourdomain.ext/somepage/`` page url to
look like.

If you don't want to deal with manually creating these files simply run ``pageup
setup`` and ``pageup`` will populate the current directory with a template.rst,
content.rst and style.css.

For an example of content.rst, template.jinja, and style.css check out the
ones in this repo.
