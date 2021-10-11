#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''A todo manager.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from time import time as _time
from time import localtime as _localtime
from sys import exit as _exit
from sys import stderr as _stderr

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
    __credits__ = '🄯 2018-2020, Louis Royer - CC0-1.0'
    __date__ = '2020-04-20'
    __version__ = '0.0.3'

def get_help():
    return '''usage: todopy [OPTION]
lists all tasks
\tcreate, --create, -c: create a todopy file for today’s tasks
\tedit, --edit, -e:     edit todays’s tasks file
\tcommit all:           commit all changes
\tpush:                 push all committed changes
\tdirectory:            print todopy’s tasks directory path (can be used as `cd $(todopy directory)`)
\tls:                   list files of tasks directory
\tll:                   list files of tasks directory as long listing format
\thelp, --help, -h:     display this help'''

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
        print(get_help())
    else:
        print(get_help(), file=_stderr)
        _exit(1)
