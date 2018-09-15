#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Reader for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from os import listdir as _listdir
import os.path as _path

import todo_parser as _todo_parser
import todo_classes as _todo_classes

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018, Louis Royer - CC0-1.0'
    __date__ = '2018-09-15'
    __version__ = '0.0.1'

filename_ignore = ('README.md',)

def print_pending_tasks(directory='/home/stri/Documents/S5/agenda'):
    for name in _listdir(directory):
        if _path.isfile(_path.join(directory, name)):
            if name not in filename_ignore:
                print('#', _path.splitext(name)[0], '\n')
                with open(filepath, mode='r') as f:
                    for line in f:
                        if _todo_parser.is_task(line):
                            if _todo_parser.get_status(line) == 'pending':
                                prev_was_task = True
                                print('-', _todo_parser.get_title)
                            else:
                                prev_was_task = False
                        elif prev_was_task:
                            if line.replace(' ', ''):
                                print(line)
                            else:
                                prev_was_task = False
                                print('')
            
