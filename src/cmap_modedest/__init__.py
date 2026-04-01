# CMAP Trip-based model tools

from importlib.metadata import version
from .cmap_logging import *
from .numexpr_patch import CacheDictSafe

__version__ = version(__name__)
