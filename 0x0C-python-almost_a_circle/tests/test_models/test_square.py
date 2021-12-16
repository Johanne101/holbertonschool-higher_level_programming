#!/usr/bin/python3
""" Test set for Square Class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os


class TestSquare(unittest.TestCase):
    """ Test cases for class Square """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Clean test files """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_id_default(self):
        s = Square(7, 4)
        self.assertEqual(s.id, 1)

    def test_size(self):
        s_size = Square(7)
        self.assertEqual(s_size.size, 7)

    def test_width_height_x(self):
        s_cero = Square(7, 4)
        self.assertEqual(s_cero.size, 7)
        self.assertEqual(s_cero.x, 4)

    def test_x_y_default(self):
        s_one = Square(28, 7, 4)
        self.assertEqual(s_one.x, 7)
        self.assertEqual(s_one.y, 4)

    def test_wrong_type_y(self):
        with self.assertRaises(TypeError):
            s_wrong_type_y = Square(1, 2, "3")

    def test_all_data_ok(self):
        s_all_data_ok = Square(1, 2, 3, 4)
        self.assertEqual(s_all_data_ok.size, 1)
        self.assertEqual(s_all_data_ok.x, 2)
        self.assertEqual(s_all_data_ok.y, 3)
        self.assertEqual(s_all_data_ok.id, 4)

    def test_wrong_sign_y(self):
        with self.assertRaises(ValueError):
            s_wrong_sign_y =  Square(1, 2, -3)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            s_zero_size =  Square(0)

    def test_instance(self):
        s_instance = Square(10, 12)

        self.assertIsInstance(s_instance, Square)
        self.assertIsInstance(s_instance, Rectangle)
        self.assertIsInstance(s_instance, Base)
        self.assertTrue(issubclass(type(s_instance), Base))
        self.assertTrue(issubclass(type(s_instance), Rectangle))
        self.assertEqual(type(s_instance), Square)
        self.assertTrue(type(s_instance) == Square)
        self.assertFalse(type(s_instance) == Rectangle)
        self.assertFalse(type(s_instance) == Base)

    def test_value_error_size(self):
        with self.assertRaises(ValueError):
            s_negative = Square(-7)

    def test_value_error_x(self):
        with self.assertRaises(ValueError):
            s_negative_x = Square(7, -4)

    def test_type_error_string_size(self):
        with self.assertRaises(TypeError):
            s_string = Square("seven")

    def test_type_error_string_x(self):
        with self.assertRaises(TypeError):
            s_string = Square(7, "four")

    def test_type_error_list(self):
        with self.assertRaises(TypeError):
            s_list = Square([7, 4], 2, 8)

    def test_area_success(self):
        s_area = Square(7, 0, 0)
        self.assertEqual(s_area.area(), 49)

    def test_area_fail(self):
        s_area = Square(7, 0, 0)
        self.assertNotEqual(s_area.area(), 28)
