'''Test module for rectangle.py'''
import unittest
from models.rectangle import rectangle


class TestRectangleGetters(unittest.TestCase):
    '''Test class for testing rectangle.py'''

    def setUp(self):
        '''Create instances of Rectangle class for testing'''

        self.one = Rectangle(2, 10, 0, 0, 5)
        
    def tearDown(self):
        '''Delete instances of Rectangle class'''
        del self.one

    def test_width(self):
        '''Tests getter and setter for width'''
        self.assertEqual(self.one.width(), 2)
        self.one.width(5)
        self.assertEqual(self.one.width(), 5)
        self.one.width(-4)
        self.assertEqual(self.one.width(), -4)

    def test_height(self):
        '''Tests getter and setter for height'''
        self.assertEqual(self.one.height(), 10)
        self.one.height(4)
        self.assertEqual(self.one.height(), 4)
        self.one.height(-7)
        self.assertEqual(self.one.height(), -7)

    def test_x(self):
        '''Tests getter and setter for x'''
        self.assertEqual(self.one.x(), 0)
        self.one.x(3)
        self.assertEqual(self.one.x(), 3)
        self.one.x(10)
        self.assertEqual(self.one.x(), 10)

    def test_y(self):
        '''Tests getter and setter for y'''
        self.assertEqual(self.one.y(), 0)
        self.one.y(9)
        self.assertEqual(self.one.y(), 9)
        self.one.y(-1)
        self.assertEqual(self.one.y(), -1)
