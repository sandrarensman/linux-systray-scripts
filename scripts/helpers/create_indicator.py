#!/usr/bin/env python3

import signal

from gi.repository import Gtk

from helpers.activate_trackball_scrolling import activate_trackball_scrolling
from helpers.indicator import Indicator


def create_indicator(filename):
    if 'trackball_scrolling' in filename:
        activate_trackball_scrolling(filename=filename)
    Indicator(filename=filename)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()
