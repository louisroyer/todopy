#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Reader for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os.path as _path
from subprocess import call as _call

if __package__:
    from . import todo_conf_reader as _todo_conf
else:
    import todo_conf_reader as _todo_conf

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018-2020, Louis Royer - CC0-1.0'
    __date__ = '2020-02-04'
    __version__ = '0.0.1'


def commit_all(directory=_todo_conf.get_directory(time=None)):
    if time is not None:
        filepath = _path.join(directory, ''.join((_strftime('%Y_%m_%d', time), '.md')))
        _call(['git', 'add', filepath])
    _call(['git', '-C', directory, '-am'])
