#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Git support for todopy.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from subprocess import call as _call
from time import strftime as _strftime

if __package__:
    from . import todo_conf_reader as _todo_conf
else:
    import todo_conf_reader as _todo_conf

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018-2020, Louis Royer - CC0-1.0'
    __date__ = '2020-02-04'
    __version__ = '0.0.1'


def commit_all(time=None, directory=_todo_conf.get_directory()):
    if time is not None:
        filepath = ''.join((_strftime('%Y_%m_%d', time), '.md'))
        _call(['git', '-C', directory, 'add', filepath])
    _call(['git', '-C', directory, 'commit', '-a'])

def push(directory=_todo_conf.get_directory()):
    _call(['git', '-C', directory, 'push'])
