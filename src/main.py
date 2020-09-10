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
    from .lib import todo_shell as _shell
else:
    from lib import todo_files_reader as _files_r
    from lib import todo_files_writer as _files_w
    from lib import todo_git as _git
    from lib import todo_shell as _shell

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018-2020, Louis Royer - CC0-1.0'
    __date__ = '2020-04-20'
    __version__ = '0.0.3'

def main(arg=None):
    if arg is None:
        _files_r.print_pending_tasks()
    elif arg in ('create', '--create', '-c'):
        _files_w.create_file(_localtime(_time()))
    elif arg in ('edit', '--edit', '-c'):
        _files_w.edit_file(_localtime(_time()))
    elif arg == 'commit all':
        _git.commit_all(_localtime(_time()))
    elif arg == 'push':
        _git.push()
    elif arg == 'directory':
        _shell.directory()
    elif arg == 'ls':
        _shell.ls()
    elif arg == 'll':
        _shell.ll()
    elif arg in ('help', '-h', '--help'):
        print('usage: todopy [OPTION]')
        print('lists all tasks')
        print('\tcreate, --create, -c: create a todopy file for today’s tasks')
        print('\tedit, --edit, -e:     edit todays’s tasks file')
        print('\tcommit all:           commit all changes')
        print('\tpush:                 push all committed changes')
        print('\tdirectory:            print todopy’s tasks directory path (can be used as `cd $(todopy directory)`)')
        print('\tls:                   list files of tasks directory')
        print('\tll:                   list files of tasks directory as long listing format')
        print('\thelp, --help, -h:     display this help')
