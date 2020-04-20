#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Shell commands support for todopy.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from subprocess import call as _call

if __package__:
    from . import todo_conf_reader as _todo_conf
else:
    import todo_conf_reader as _todo_conf

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018-2020, Louis Royer - CC0-1.0'
    __date__ = '2020-04-20'
    __version__ = '0.0.1'

def directory():
    print(_todo_conf.get_directory())

def ls():
    _call(['ls', _todo_conf.get_directory()])

def ll():
    _call(['ls', '-l', _todo_conf.get_directory()])
