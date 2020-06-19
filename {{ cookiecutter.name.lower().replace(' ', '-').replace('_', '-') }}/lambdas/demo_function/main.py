"""Main.

This is the main entry point for this application.
"""

import json
import logging

try:
    from config import Config
    from app import App
except ImportError:
    from .config import Config
    from .app import App

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def lambda_handler(event: dict = None, context=None):
    """Lambda Handler."""

    config = Config()

    log.info(f'App Version: {config.version}')
    log.info(f'Event: {json.dumps(event, indent=2)}')

    app = App()
    # TODO: Call functionality here.
