"""Config.

Provides configuration for the application.
"""

import os
from dataclasses import dataclass

try:
    from __version__ import __version__
except ImportError:
    from .__version__ import __version__


@dataclass
class Config:
    version: str = __version__
    # TODO: Define additional config here.
