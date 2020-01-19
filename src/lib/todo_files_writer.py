#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Writer for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os.path as _path

from subprocess import call as _call
from time import strftime as _strftime
if __package__:
    from . import todo_conf_reader as _todo_conf
else:
    import todo_conf_reader as _todo_conf
if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018-2020, Louis Royer - CC0-1.0'
    __date__ = '2020-01-19'
    __version__ = '0.0.2'

def create_file(time: tuple, directory=_todo_conf.get_directory()):
    filepath = _path.join(directory, ''.join((_strftime('%Y_%m_%d', time), '.md')))
    with open(filepath, mode='x') as f:
        f.write(''.join(('# Séance du ', _strftime('%Y-%m-%d', time))))

def edit_file(time: tuple, directory=_todo_conf.get_directory()):
    filepath = _path.join(directory, ''.join((_strftime('%Y_%m_%d', time), '.md')))
    try:
        create_file(time, directory)
    except FileExistsError:
        pass
    _call(['editor', filepath])
