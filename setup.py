from distutils.core import setup

setup(
    name='pageup',
    version='0.4',
    packages=['pageup'],
    author='Elijah Caine',
    author_email='elijahcainemv@gmail.com',
    url='https://github.com/ElijahCaine/pageup',
    description='A simple RST based static (html) page generator,',
    install_requires=[
                      'docutils==0.12',
                      'Jinja2==2.7.3',
                      'MarkupSafe==0.23',
                      'requests==2.7.0',
                     ],
    scripts=['pageup/pageup'],
    data_files=[('data', ['pageup/data/template.jinja',
                          'pageup/data/style.css',
                          'pageup/data/content.rst'])]
)
