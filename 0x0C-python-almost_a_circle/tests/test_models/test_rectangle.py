'''Test module for rectangle.py'''
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    '''Test class to test Rectangle module'''

    def setUp(self):
        '''Set up instances in order to run tests'''
        self.one = Rectangle(2, 5)
        self.two = Rectangle(2, 5, 1)
        self.three = Rectangle(2, 5, 1, 2)
        self.four = Rectangle(2, 5, 1, 2, 98)

    def tearDown(self):
        '''Delete instances once tests are done'''
        del self.one
        del self.two
        del self.three
        del self.four

    # TODO:
    # check class documentation exists      Done
    # check if function documentation exists
    # check instantiation
    # check attribute values
    # check exceptions on variables
    # check method return values
    # check exceptions

    def test_for_class_docs(self):
        '''Tests to see if class documentation is present

        Return:
            function self.assertIsNotNone returns true if self.__doc__ is not
            None, meaning that documentation exists for class
            else if documentation does not exists, returns false
        '''
        self.assertIsNotNone(self.__doc__)

    def test_for_method_docs(self):
        '''Tests to see if method documentation exists for methods
        contained in the class

        Return:
            True if self.<methodName>.__doc__ is not None
            False if method does not have documentation
        '''
        # test constructor method for documentation
        self.assertIsNotNone(self.__init__.__doc__)

        # test getters and setter for documentation
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)

        # test static and class methods for documentation
        self.assertIsNotNone(self.two.to_json_string.__doc__)
        self.assertIsNotNone(Rectangle.save_to_file.__doc__)
        self.assertIsNotNone(self.one.from_json_string.__doc__)
        self.assertIsNotNone(Rectangle.create.__doc__)
        self.assertIsNotNone(Rectangle.load_from_file.__doc__)

    def test_instantiation(self):
        '''Tests instances of Rectangle class'''
        self.assertTrue(isinstance(self.one, Rectangle))
        self.assertTrue(isinstance(self.one, Rectangle))
        self.assertTrue(isinstance(self.two, Rectangle))
        self.assertTrue(isinstance(self.three, Rectangle))

    def test_field_attributes(self):
        '''Tests the class and instance variables'''
        self.assertEqual(self.four.id, 98)
        self.assertEqual(self.one.width, 2)
        self.assertEqual(self.two.height, 5)
        self.assertEqual(self.three.x, 1)
        self.assertEqual(self.four.y, 2)
        self.assertEqual(self.one.x, 0)
        self.assertEqual(self.one.y, 0)

    def test_exceptions_for_field_atts(self):
        '''Tests exception cases for class and instance variables'''

        # tests for width and height exceptions
        
        with self.assertRaises(ValueError):
            obj = Rectangle(-1, 5)
        with self.assertRaises(ValueError):
            obj = Rectangle(5, 0)
        with self.assertRaises(TypeError):
            obj = Rectangle(None, 5)
        with self.assertRaises(TypeError):
            obj = Rectangle(1, "hi")
        with self.assertRaises(TypeError):
            obj = Rectangle(7, 2.5)
        with self.assertRaises(TypeError):
            obj = Rectangle(13, [])
        with self.assertRaises(TypeError):
            obj = Rectangle(3, {})
        with self.assertRaises(TypeError):
            obj = Rectangle(5, (1, 2))
        with self.assertRaises(TypeError):
            obj = Rectangle(2.5j, 5)

        # tests for x and y exceptions

        with self.assertRaises(TypeError):
            obj = Rectangle(1, 5, 2, 2.5)
        with self.assertRaises(TypeError):
            obj = Rectangle(5, 1, "hi", 2)
        with self.assertRaises(ValueError):
            obj = Rectangle(5, 5, 3, -2)
        with self.assertRaises(TypeError):
            obj = Rectangle(1, 2, 0, (1, 2))
        with self.assertRaises(TypeError):
            obj = Rectangle(7, 2.5, 0, [])
