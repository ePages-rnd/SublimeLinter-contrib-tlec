#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jonas Gratz
# Copyright (c) 2015 Jonas Gratz
#
# License: MIT
#

"""This module exports the Tlec plugin class."""

import sublime
from SublimeLinter.lint import Linter, util

class Tlec(Linter):

    """Provides an interface to tlec."""

    def cmd(self):
        return [self.executable_path, sublime.load_settings('Epages6.sublime-settings').get('path'), '--vm=' + self.view.settings().get('ep6_vm'), '--lint', '@'];

    executable = 'perl'
    syntax = ('html', 'tle')
    regex = r'(?P<message>.+?) at line (?P<line>\d+)(, near (?P<near>.+?))?'
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'html'
