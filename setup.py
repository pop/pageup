from distutils.core import setup


with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]


setup(
    name='pageup',
    version='0.1',
    packages=['pageup'],
    author='Elijah Caine',
    author_email='elijahcainemv@gmail.com',
    url='https://github.com/ElijahCaine/pageup',
    description='A simple RST based static (html) page generator,',
    install_requires=requirements,
    scripts=['pageup/pageup'],
)
