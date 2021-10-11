#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Reader for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from xdg import BaseDirectory as _basedir
from toml import decoder as _decoder
from os import path as _path

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🄯 2021, Louis Royer - CC0-1.0'
    __date__ = '2021-10-11'
    __version__ = '0.0.1'

soft_name = 'todopy'
conf_file = 'config.toml'

def get_filename_ignore() -> str:
    default_ignore = ['README.md']
    try:
        conf_dir = _basedir.load_first_config(soft_name)
        if conf_dir is None:
            return default_ignore
        with open(_path.join(conf_dir, conf_file)) as f:
            c = _decoder.load(f).get('config')
            if c is not None:
                l = c.get('exclude_files')
                if l is not None:
                    return l
        return default_ignore
    except FileNotFoundError:
        return default_ignore 

def get_directory() -> str:
    default_directory = _basedir.save_data_path(soft_name)
    try:
        conf_dir = _basedir.load_first_config(soft_name)
        if conf_dir is None:
            return default_directory
        with open(_path.join(conf_dir, conf_file)) as f:
            c = _decoder.load(f).get('config')
            if c is not None:
                d = c.get('directory')
                if d is not None:
                    return _path.expandvars(_path.expanduser(d))
        return default_directory
    except FileNotFoundError:
        return default_directory

    
