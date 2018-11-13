#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Reader for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from os import listdir as _listdir
import os.path as _path
if __package__:
    from . import todo_parser as _todo_parser
    from . import todo_classes as _todo_classes
else:
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
        filepath = _path.join(directory, name)
        if _path.isfile(filepath):
            if '.md' == _path.splitext(filepath)[1]:
                if name not in filename_ignore:
                    with open(filepath, mode='r') as f:
                        prev_was_task = False
                        title_printed = False
                        for line in f:
                            line = line.replace('\n', '')
                            if _todo_parser.is_task(line):
                                if _todo_parser.get_status(line) == 'pending':
                                    prev_was_task = True
                                    if not title_printed:
                                        print('\n#', _path.splitext(name)[0].replace('_', '-'), '\n')
                                        title_printed = True
                                    print('-', _todo_parser.get_title(line))
                                else:
                                    prev_was_task = False
                            elif prev_was_task:
                                if line.replace(' ', '') != '':
                                    print(' ', line)
                                else:
                                    prev_was_task = False
                                    print('')
                
