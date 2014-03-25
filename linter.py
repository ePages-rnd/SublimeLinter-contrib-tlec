#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jonas Gratz
# Copyright (c) 2014 Jonas Gratz
#
# License: MIT
#

"""This module exports the Tlec plugin class."""

from SublimeLinter.lint import Linter, util


class Tlec(Linter):

    """Provides an interface to tlec."""

    syntax = ('html', 'tle')
    cmd = 'tlec @'
    regex = r'(?P<message>.+?) at line (?P<line>\d+)(, near (?P<near>.+?))?'
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'html'
