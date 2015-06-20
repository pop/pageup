"""
PageUp: A simple ReStructuredText based static page generator.

'It ain't supposed to be pretty, it's just supposed to work.'
    - me. right now.
"""

from docutils.core import publish_parts
from jinja2 import Environment, FileSystemLoader
import os 
import requests
import urllib


# Root directory of the app and where it is installed (system wide or in a
# virtual environment.
_ROOT = os.path.abspath(os.path.dirname(__file__))

def copy_file(src, dst):
    print "Copying {0} to {1}".format(src, dst)
    try:
        shutil.copyfile(src, dst)
    except OSError as e:
        print "Oops! There was an error copying from {0} to {1}".format(src, dst)
        print "{0}".format(e)

def copy_dir(src, dst):
    print "Copying {0} to {1}".format(src, dst)
    try:
        shutil.copytree(src, dst)
    except OSError as e:
        print "Oops! There was an error copying the files from {0} to {1}".format(src, dst)
        print "{0}".format(e)


def test_files(data_dir):
    """
    Tests to see if all of the appropriate files are in the right places.
    """
    print "Ensuring that file structure is correct..."
    yell = ''
    needed = ['template.jinja', 'content.rst', 'style.css']
    for page in needed:
        n = os.path.join(data_dir, page)
        if not os.path.isfile(n):
            yell += n + " does not appear to be available.\n"
    if yell:
        raise Exception(yell + " run `pageup init` to fix it.")
        exit(1)


def build():
    """
    Builds pages given template.jinja, style.css, and content.rst
    produces index.html.
    """
    path = os.getcwd()

    output_dir = os.path.join(path, "build")
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
        os.chmod(output_dir, 0o775)

    data_dir = os.path.join(path, "data")
    test_files(data_dir)
    print "Reading files from {0}".format(data_dir)
    content = os.path.join(data_dir, "content.rst")
    with open(content) as f:
        content = publish_parts(f.read(), writer_name='html')
        title = content['title']
        body =  content['html_body'].replace('\n',' ')
    template = os.path.join(data_dir, 'template.jinja')
    with open(template, 'r') as f:
        loader = FileSystemLoader(data_dir)
        env= Environment(loader=loader)
        template = env.get_template('template.jinja')
        page =  template.render(title=title,
                                content=body)
    index = os.path.join(output_dir, 'index.html')
    with open(index, 'w') as f:
        f.write(page)


def init(directory):
    """
    Initializes a new site in the `directory`
    Current working dir if directory is None.
    """
    if directory is not None and not os.path.exists(directory):
        os.mkdir(directory)
    else:
        print "{0} already exists, populating with template files".format(directory)
        directory = ''

    data_dir = os.path.join(directory, "data")
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
        os.chmod(data_dir, 0o775)

    if not os.path.isfile(os.path.join(data_dir,'style.css')):
        grab('style.css', data_dir)
        print('Added sample style')
    if not os.path.isfile(os.path.join(data_dir,'template.jinja')):
        grab('template.jinja', data_dir)
        print('Added sample template.jinja')
    if not os.path.isfile(os.path.join(data_dir,'content.rst')):
        grab('content.rst', data_dir)
        print('Added sample content.rst')

def grab(filename, directory):
    """
    Copy dist files from their installed path to cwd/directory/filename
    cwd is the current directory,
    directory is their custom site name dir,
    filename is the name of the example file being copied over.
    """
    write_to = os.path.join(directory,filename)
    urllib.urlretrieve('https://raw.githubusercontent.com/ElijahCaine/pageup/master/pageup/data/'+filename, write_to)

if __name__ == '__main__':
    directory = os.getcwd()
    init(directory)
    build()
