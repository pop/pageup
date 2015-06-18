from distutils.core import setup


with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]


setup(
    name='pageup',
    version='0.1',
    packages=['pageup'],
    author='Elijah Caine',
    author_email='elijahcainemv@gmail.com',
    url='https://elijahcaine.me/bookclub/',
    description='A small package for throwing together single page static sites',
    install_requires=requirements,
    scripts=['pageup/pageup'],
#    data_files=[('static', ['static/style.css',
#                            'static/content.rst',
#                            'static/template.jinja'])]
#    
)
