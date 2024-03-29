#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Classes for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
if __debug__:
    if __package__:
        from . import todo_parser as _todo_parser
    else:
        import todo_parser as _todo_parser

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🄯 2018, Louis Royer - CC0-1.0'
    __date__ = '2018-09-15'
    __version__ = '0.0.1'


class Task:
    def __init__(self, title: str, filename: str, status):
        assert status in _todo_parser.TASK_STATUS, 'Invalid status'
        self._title = title
        self._filename = filename
        self._status = status
        self._updated_status = False

    @property
    def title(self):
        '''Task title.'''
        return _title

    @property
    def filename(self):
        '''Filename where task was written.'''
        return _filename

    @property
    def status(self):
        '''Task status.'''
        return _status
    
    @status.setter
    def status(self, value):
        assert status in STATUS, 'Invalid status'
        self._updated_status = True
        self._status = value
