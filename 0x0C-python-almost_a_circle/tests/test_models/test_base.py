'''Test module for base.py'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Test class to test Base module'''
    
    def setUp(self):
        '''Set up instances in order to run tests'''
        self.one = Base()
        self.two = Base(19)
        self.three = Base(-5)
        self.four = Base(None)

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
        self.assertIsNotNone(self.__init__.__doc__)
        self.assertIsNotNone(self.two.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_instantiation(self):
        '''Tests instances of Base class'''
        self.assertTrue(isinstance(self.one, Base))
        self.assertTrue(isinstance(self.two, Base))
        self.assertTrue(isinstance(self.three, Base))

    def test_field_attributes(self):
        '''Tests the class and instance variables'''
        self.assertEqual(self.one.id, 1)
        self.assertEqual(self.two.id, 19)
        self.assertEqual(self.three.id, -5)
        self.assertEqual(self.four.id, 2)

    def test_method_returns(self):
        '''Tests the return values for the static methods'''

        # set up two dictionaries
        dict_one = {"id":self.one.id}
        dict_two = {}
        list_dict = [dict_one, dict_two]

        # convert list of dictionaries to json string
        self.assertTrue(isinstance(Base.to_json_string(list_dict), str))

        # convert json string basck to list of dictionaries
        json_str = Base.to_json_string(list_dict)
        self.assertTrue(Base.from_json_string(json_str) ==  list_dict)
