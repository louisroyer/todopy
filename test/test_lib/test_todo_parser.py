#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Test file'''

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import unittest
from src.lib import todo_parser as _todo_parser

__author__ = 'Louis Royer'
__credits__ = '🅬 2018, Louis Royer - CC0-1.0'
__date__ = '2018-07-08'
__version__ = '0.0.1'

class TestStrTodoDone(unittest.TestCase):
    '''Test a string representing a task done.'''

    @classmethod
    def setUpClass(cls):
        cls._test_strings = ('[x] my task done',
                '[ x ] my task done',
                ' [ x ] my task done',
                '-[x] my task done',
                '- [x] my task done',
                '- [ x ] my task done',
                ' - [x] my task done',
                ' -[x] my task done',
                ' - [ x ] my task done',
                ' -[ x ] my task done',
                '[x]my task done',
                '[ x ]my task done',
                ' [ x ]my task done',
                '-[x]my task done',
                '- [x]my task done',
                '- [ x ]my task done',
                ' - [x]my task done',
                ' -[x]my task done',
                ' - [ x ]my task done',
                ' -[ x ]my task done')
        cls._test_task_title = 'my task done'
        cls._test_task_status = 'done'
        assert cls._test_task_status in _todo_parser.TASK_STATUS, 'Invalid status'

    def test_is_task(self):
        '''Test the function is_task.'''
        for string in self._test_strings:
            with self.subTest(string=string):
                self.assertEqual(_todo_parser.is_task(string), True)

    def test_title(self):
        '''Test the function get_title.'''
        for string in self._test_strings:
            with self.subTest(string=string):
                self.assertEqual(_todo_parser.get_title(string), self._test_task_title)

    def test_status(self):
        '''Test the function get status.'''
        for string in self._test_strings:
            with self.subTest(string=string):
                self.assertEqual(_todo_parser.get_status(string), self._test_task_status)



class TestStrTodoPending(unittest.TestCase):
    '''Test a string representing a task pending.'''
   
    @classmethod
    def setUpClass(cls):
        cls._test_strings = ('[] my pending task',
                '[ ] my pending task',
                ' [] my pending task',
                ' [ ] my pending task',
                '-[] my pending task',
                '-[ ] my pending task',
                '- [] my pending task',
                '- [ ] my pending task',
                ' -[] my pending task',
                ' - [] my pending task',
                ' -[ ] my pending task',
                ' - [ ] my pending task',
                '[]my pending task',
                '[ ]my pending task',
                ' []my pending task',
                ' [ ]my pending task',
                '-[]my pending task',
                '-[ ]my pending task',
                '- []my pending task',
                '- [ ]my pending task',
                ' -[]my pending task',
                ' - []my pending task',
                ' -[ ]my pending task',
                ' - [ ]my pending task')
        cls._test_task_title = 'my pending task'
        cls._test_task_status = 'pending'
        assert cls._test_task_status in _todo_parser.TASK_STATUS, 'Invalid status'

    def test_is_task(self):
        '''Test the function is_task.'''
        for string in self._test_strings:
            with self.subTest(string=string):
                self.assertEqual(_todo_parser.is_task(string), True)

    def test_title(self):
        '''Test the function get_title.'''
        for string in self._test_strings:
            with self.subTest(string=string):
                self.assertEqual(_todo_parser.get_title(string), self._test_task_title)

    def test_status(self):
        '''Test the function get status.'''
        for string in self._test_strings:
            with self.subTest(string=string):
                self.assertEqual(_todo_parser.get_status(string), self._test_task_status)

class TestStrNotATask(unittest.TestCase):
    '''Test a string not representing a task.'''

    @classmethod
    def setUpClass(cls):
        cls._test_strings = ('not a task',
                '#Title',
                '- item not a task',
                '[Title](link)',
                '[x](link)',
                'text with a []',
                '[](link without title)',
                'text with a [x]')

    def test_is_task(self):
        '''Test the function is_task.'''
        for string in self._test_strings:
            with self.subTest(string=string):
                self.assertEqual(_todo_parser.is_task(string), False)
