#!/usr/bin/python3
""" Unittest for Base Class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import json
import pep8


class TestBase(unittest.TestCase):
    """ Unittest for Base Class """

    def test_pep8(self):
        """test that we comply with PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        "tests/test_models/test_base.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    def setUpCls(self):
        """Seting up the objects or instances to be tested
        """
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(100)
        self.b4 = Base()
        self.b5 = Base(200)
        self.b6 = Base("string")

    def test_to_json_string(self):
        """test to
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'string': 10}]), '[{"string": 10}]')
        self.assertEqual(type(Base.to_json_string([{'string': 10}])), str)

    def test_from_json_string(self):
        """test from
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"string": 10}]'), [{'hey': 10}])
        self.assertEqual(type(Base.from_json_string('[{"string": 10}]')), list)
