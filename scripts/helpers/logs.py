#!/usr/bin/env python3

import logging

import gi
from pathlib import Path

gi.require_version('Gtk', '3.0')

from datetime import datetime

logfile = './systray-scripts.log'

def logger(file):
    logging.basicConfig(filename=logfile.lstrip('./'), level=logging.DEBUG, 
                        format='%(asctime)s %(levelname)s %(process)d %(name)s %(message)s')
    return logging.getLogger(file)

def cleanup_logs():
    if Path(logfile).exists():
        with open(logfile, "r") as file:
            lines = [line.rstrip() for line in file]

        date_format = '%Y-%m-%d'
        today = datetime.today()

        new_log = []
        for line in lines:
            log_date = datetime.strptime(line.split(' ')[0], date_format)
            delta = today - log_date
            if delta.days < 90:
                new_log.append(line)

        with open(logfile, 'w') as file:
            for line in new_log:
                file.write('{}\n'.format(line))
    else:
        return
