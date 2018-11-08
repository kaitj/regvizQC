from distutils.core import setup
from regvizQC._version import __version__

setup(
    # Project information
    name='regvizQC',
    version=__version__,
    description='Create gifs to quickly qualitatively assess registrations',
    packages=['regvizQC',
              'regvizQC/interfaces'],
    scripts=['regvizQC/pipelines/regvizQC'],

    # Metadata
    author='Jason Kai',
    author_email='tkai@uwo.ca'
)
