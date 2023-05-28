#!/bin/env python
import os
from dotenv import load_dotenv
from pathlib import Path

APP_ROOT = os.path.join(os.path.dirname(__file__))
CONFIG_DIR = Path(APP_ROOT) / 'config'
load_dotenv(CONFIG_DIR / '.env')

os.environ["APP_ROOT"] = APP_ROOT
os.environ["CONFIG_DIR"] = str(CONFIG_DIR)

import src.app