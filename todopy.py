#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''A todolist manager.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from sys import argv as _argv
# begin modules imports
from src.main import *
# end modules imports

__author__ = 'Louis Royer'
__credits__ = '🅬 2018, Louis Royer - CC0-1.0'
__date__ = '2018-09-15'
__version__ = '0.0.1'

try:
    main(_argv[1] + ' ' + _argv[2])
except IndexError:
    try:
        main(_argv[1])
    except IndexError:
        main()
