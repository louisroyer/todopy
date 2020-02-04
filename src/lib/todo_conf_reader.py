#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Reader for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from dirspec import basedir as _basedir
from toml import decoder as _decoder

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2020, Louis Royer - CC0-1.0'
    __date__ = '2020-01-19'
    __version__ = '0.0.1'

soft_name = 'todopy'
conf_file = 'config.toml'

def get_filename_ignore() -> str:
    try:
        conf = _basedir.load_config_paths(soft_name)
        for p in conf:
            with open('/'.join([str(p, 'utf-8'), conf_file])) as f:
                c = _decoder.load(f).get('config')
                if c is not None:
                    l = c.get('exclude_files')
                    if l is not None:
                        return l
        #default
        return ['README.md']
    except FileNotFoundError:
        return ['README.md']

def get_directory() -> str:
    try:
        conf = _basedir.load_config_paths(soft_name)
        for p in conf:
            with open('/'.join([str(p, 'utf-8'), conf_file])) as f:
                c = _decoder.load(f).get('config')
                if c is not None:
                    d = c.get('directory')
                    if d is not None:
                        return d
        #default
        return str(_basedir.save_data_path(soft_name), 'utf-8')
    except FileNotFoundError:
        return str(_basedir.save_data_path(soft_name), 'utf-8')

    
