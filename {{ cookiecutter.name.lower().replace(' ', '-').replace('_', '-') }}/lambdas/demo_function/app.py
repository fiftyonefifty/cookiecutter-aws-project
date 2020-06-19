"""App"""

import logging

import boto3
from botocore.exceptions import ClientError

try:
    from config import Config
except ImportError:
    from .config import Config

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class App:
    def __init__(self, config: Config):
        self.config = config

    # TODO: Add functionality here.
