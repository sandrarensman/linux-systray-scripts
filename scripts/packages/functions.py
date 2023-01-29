#!/usr/bin/env python3

import logging

import gi

gi.require_version('Gtk', '3.0')
import signal

from gi.repository import Gtk

from packages.indicator import Indicator


def logger(file):
    file_name = file.split('/')[-1]
    logging.basicConfig(filename='logfile.log', level=logging.DEBUG, 
                        format='%(asctime)s %(levelname)s %(process)d %(name)s %(message)s')
    return logging.getLogger(file_name)

def get_filename(filepath):
    file = filepath.split('/')[-1]
    filename = file.split('.')[0]
    return filename

def create_indicator(filepath):
    Indicator(name=get_filename(filepath))
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()
