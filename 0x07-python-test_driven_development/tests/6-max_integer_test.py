#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Class to test max_integer'''
    def test_value(self):
        '''Function to test results of max_integer'''
        self.assertEqual(max_integer([5, 4, 6]), 6)
        self.assertEqual(max_integer([-1, -5, -10]), -1)
        self.assertEqual(max_integer([2.5, 4, 3.5]), 4)
        self.assertEqual(max_integer([]), None)
