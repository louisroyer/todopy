#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''A todo manager.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from time import time as _time
from time import localtime as _localtime

if __package__:
    from .lib import todo_files_reader as _files_r
    from .lib import todo_files_writer as _files_w
    from .lib import todo_git as _git
else:
    from lib import todo_files_reader as _files_r
    from lib import todo_files_writer as _files_w
    from lib import todo_git as _git

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018-2020, Louis Royer - CC0-1.0'
    __date__ = '2020-01-19'
    __version__ = '0.0.2'

def main(arg=None):
    if arg is None:
        _files_r.print_pending_tasks()
    elif arg == 'create':
        _files_w.create_file(_localtime(_time()))
    elif arg == 'edit':
        _files_w.edit_file(_localtime(_time()))
    elif arg == 'commit all':
        _git.commit_all(_localtime(_time()))

