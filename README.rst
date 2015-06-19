================================
``pageup init`` ``pageup build``
================================

Yes, that easy
--------------

``pageup`` is a little tool get your (web)page up asap. ``pageup init
yoursite``, then run ``pageup build`` after you've made changes to your content
and page styles. I use this to manage my `book club`_ website and a few other
single page static pages.

Made with `jinja2`_ and `docutils`_.

.. _book club: http://elijahcaine/reading/
.. _jinja2: http://jinja.pocoo.org/
.. _docutils: http://docutils.sourceforge.net/


Usage
-----
``pageup`` is pretty simple. 

======================  ==============================================================================
Command                 Description
======================  ==============================================================================
``pageup``              Prints help menu.
``pageup build``        Generates the page in the site's base directory. Generates an index.html file.
``pageup init``         Populates current working directory with necessary files
``pageup init mysite``  Creates ``mysite`` directory and populates that with necessary files.
======================  ==============================================================================

Necessary files are ``content.rst``, ``style.css``, and ``template.jinja``.
These are templates for you to modify.


Installation:
-------------

.. code::

    $ pip install pageup
    or
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
