#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Writer for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import os.path as _path
from time import strftime as _strftime
if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018, Louis Royer - CC0-1.0'
    __date__ = '2018-10-14'
    __version__ = '0.0.1'

def create_file(time: tuple, directory='/home/stri/Documents/S5/agenda'):
    filepath = _path.join(directory, ''.join((_strftime('%Y_%m_%d', time), '.md')))
    with open(filepath, mode='x') as f:
        f.write('# Séance du', _strftime('%Y_%m_%d', time))

