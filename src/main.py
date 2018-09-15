#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''A todo manager.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from lib import todo_files_reader as _files_r
if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018, Louis Royer - CC0-1.0'
    __date__ = '2018-09-15'
    __version__ = '0.0.1'


_files_r.print_pending_tasks()
