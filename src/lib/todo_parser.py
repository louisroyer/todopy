#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Parser for todo files.'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

if __name__ != '__main__':
    __author__ = 'Louis Royer'
    __credits__ = '🅬 2018, Louis Royer - CC0-1.0'
    __date__ = '2018-09-15'
    __version__ = '0.0.1'


def is_task(string: str) -> bool:
    '''Return True if the string is a task.'''
    index_bracket_opens = string.find('[')
    index_bracket_closes = string.find(']')
    if index_bracket_opens == -1 or index_bracket_closes == -1:
        return False
    for i in range(0, index_bracket_opens):
        if string[i] not in ('-', ' '):
            return False
    for i in range(index_bracket_opens + 1, index_bracket_closes):
        if string[i] not in ('x', ' '):
            return False
    try:
        if string[index_bracket_closes + 1:index_bracket_closes +2] == ' (':
            if ')' in string[index_bracket_closes +3:]:
                return False
    except IndexError:
        pass

    try:
        if string[index_bracket_closes + 1] == '(':
            if ')' in string[index_bracket_closes +2:]:
                return False
    except IndexError:
        pass

    return True

def get_title(string: str) -> str:
    '''Return the title of a task.'''
    assert is_task(string) == True
    begin = string.find(']') + 1
    for i, letter in enumerate(string[begin:]):
        if letter != ' ':
            title_starts = i
            break
    return string[begin+i:]

