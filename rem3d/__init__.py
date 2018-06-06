from __future__ import absolute_import
from os.path import dirname, basename, isfile
import glob
import pkgutil 

from .version import version as __version__

#### Import all modules below
# constants: constant for downloads etc.
# tools: generic tools library
# data: data analyses library
# models: models library
# plots: plotting library

__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
    __import__(modname)
