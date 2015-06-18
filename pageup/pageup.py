"""
Reading Club
Hosted on http://elijahcaine.me/bookclub/

'It ain't supposed to be pretty, it's just supposed to work.'
    - me. right now.
"""

from docutils.core import publish_parts
from jinja2 import Environment, FileSystemLoader
from os import getcwd, path
import requests


_ROOT = path.abspath(path.dirname(__file__))



def test_files():
    yell = ''
    needed = ['template.jinja', 'content.rst', 'style.css']
    for n in needed:
        if not path.isfile(n):
            yell += n + " does not appear to be available.\n"
    if yell:
        raise Exception(yell + " run `pageup init` to fix it.")
        exit(1)


def build():
    test_files()
    with open('content.rst') as f:
        content = publish_parts(f.read(), writer_name='html')
        title = content['title']
        body =  content['html_body'].replace('\n',' ')

    with open('template.jinja', 'r') as f:
        loader = FileSystemLoader(getcwd())
        env= Environment(loader=loader)
        template = env.get_template('template.jinja')
        page =  template.render(title=title,
                                content=body)

    with open('index.html', 'w') as f:
        f.write(page)


def init():
    if not path.isfile("style.css"):
        grab('style.css')
        print("Added sample style")
    if not path.isfile("template.jinja"):
        grab('template.jinja')
        print("Added sample template.jinja")
    if not path.isfile("content.rst"):
        grab('content.rst')
        print("Added sample content.rst")

def grab(filename):
    print("Copying %s from %s to %s" % (filename, path.join(_ROOT, 'data', filename), path.join(getcwd(), filename)))
    with open(path.join(getcwd(), filename), 'w') as copy:
        with open(path.join(_ROOT, 'data', filename), 'r') as template:
            for line in template:
                copy.write(line)
