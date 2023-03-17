#!/usr/bin/env python3

from pathlib import Path

from helpers.create_indicator import create_indicator
from helpers.logs import cleanup_logs

if __name__ == '__main__':
    cleanup_logs()
    filename = Path(__file__).name
    create_indicator(filename)
