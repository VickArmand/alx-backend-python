#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function
and understand its purpose.
Play with it in the Python console to make sure you understand.
"""
import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    inherits from unittest.TestCase
    In this task you will write the first unit test
    for utils.access_nested_map.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        method to test that the utils.access_nested_map method
        returns what it is supposed to
        Decorate the method with @parameterized.expand
        to test the function for following inputs:
        nested_map={"a": 1}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a", "b")
        For each of these inputs, test with assertEqual that the function
        returns the expected result.
        The body of the test method should not be longer than 2 lines.
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Use the assertRaises context manager to test
        that a KeyError is raised for the
        following inputs (use @parameterized.expand)
        nested_map={}, path=("a",)
        nested_map={"a": 1}, path=("a", "b")
        """
        self.assertRaises(utils.access_nested_map(nested_map, path), expected)
