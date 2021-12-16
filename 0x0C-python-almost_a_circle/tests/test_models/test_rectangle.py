#!/usr/bin/python3
""" Test set for rectangle Class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestRectangle(unittest.TestCase):
    """ Test cases for class rectangle """

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Clean test files """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")

    def test_id_default(self):
        r = Rectangle(7, 4)
        self.assertEqual(r.id, 1)

    def test_width_height(self):
        r_cero = Rectangle(7, 4)
        self.assertEqual(r_cero.width, 7)
        self.assertEqual(r_cero.height, 4)

    def test_x_y_default(self):
        r_one = Rectangle(7, 4)
        self.assertEqual(r_one.x, 0)
        self.assertEqual(r_one.y, 0)

    def test_instance(self):
        r_instance = Rectangle(7, 4)

        self.assertIsInstance(r_instance, Rectangle)
        self.assertIsInstance(r_instance, Base)
        self.assertTrue(issubclass(type(r_instance), Base))
        self.assertTrue(issubclass(type(r_instance), Rectangle))
        self.assertTrue(type(r_instance) == Rectangle)
        self.assertFalse(type(r_instance) == Base)

    def test_value_error_width(self):
        with self.assertRaises(ValueError):
            r_negative_w = Rectangle(-7, 4)

    def test_value_error_height(self):
        with self.assertRaises(ValueError):
            r_negative_h = Rectangle(7, -4)

    def test_type_error_string_width(self):
        with self.assertRaises(TypeError):
            r_string = Rectangle("seven", 4)

    def test_type_error_string_heigth(self):
        with self.assertRaises(TypeError):
            r_string = Rectangle(7, "four")

    def test_type_error_list(self):
        with self.assertRaises(TypeError):
            r_list = Rectangle([7, 4], 28, 0, 0)

    def test_area_success(self):
        r_area = Rectangle(7, 4, 0, 0, 28)
        self.assertEqual(r_area.area(), 28)

    def test_area_fail(self):
        r_area = Rectangle(7, 7, 0, 0, 28)
        self.assertNotEqual(r_area.area(), 28)

    def test_wrong_type_04(self):
        with self.assertRaises(TypeError):
            r_wrong_type = Rectangle(1, 2, 3, "4")

    def test_all_data(self):
        r_all_data = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r_all_data.id, 5)

    def test_cero_param_w(self):
        with self.assertRaises(ValueError):
            r_cero_width = Rectangle(0, 2)

    def test_cero_param_h(self):
        with self.assertRaises(ValueError):
            r_cero_height = Rectangle(1, 0)

    def test_value_error_y(self):
        with self.assertRaises(ValueError):
            r_value_error_y =  Rectangle(1, 2, 3, -4)
