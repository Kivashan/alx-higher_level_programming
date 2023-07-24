'''Test module for base.py'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Test class to test Base module'''

    def setUp(self):
        '''Set up instances in order to run tests'''
        self.one = Base()
        self.two = Base()
        self.three = Base(19)
        self.four = Base(-5)
        self.five = Base()
        self.six = Base(0)

    def tearDown(self):
        '''Delete instances once tests are done'''
        del self.one
        del self.two
        del self.three
        del self.four
        del self.five
        del self.six

    def test_id(self):
        '''Test the value of id attribute of Base class'''
        self.assertEqual(self.one.id, 1)
        self.assertEqual(self.two.id, 2)
        self.assertEqual(self.three.id, 19)
        self.assertEqual(self.four.id, -5)
        self.assertEqual(self.five.id, 3)
        self.assertEqual(self.six.id, 0)
