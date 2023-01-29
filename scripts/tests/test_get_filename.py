#!/usr/bin/env python3

from packages import functions


def test_get_filename():
    assert type(functions.get_filename(__file__)) == str
