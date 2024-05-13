#!/usr/bin/env python3
"""
test_utils module has test classes
for testing the utils module
"""
import unittest
from unittest.mock import patch
import utils
import requests
from utils import memoize
from typing import Mapping, Sequence, Union, Dict
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
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Union[int, Dict]) -> None:
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
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Use the assertRaises context manager to test
        that a KeyError is raised for the
        following inputs (use @parameterized.expand)
        nested_map={}, path=("a",)
        nested_map={"a": 1}, path=("a", "b")
        """
        with self.assertRaises(Exception):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    tests the utils.get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, expected_payload, mock_get):
        """
        We don’t want to make any actual external HTTP calls.
        Use unittest.mock.patch to patch requests.get.
        Make sure it returns a Mock object with a json method that
        returns test_payload which you parametrize alongside the
        test_url that you will pass to get_json with the following inputs:
        test_url="http://example.com", test_payload={"payload": True}
        test_url="http://holberton.io", test_payload={"payload": False}
        Test that the mocked get method was called exactly once (per input)
        with test_url as argument.
        Test that the output of get_json is equal to test_payload.
        """
        mock_get.return_value.json.return_value = expected_payload
        result = utils.get_json(url)
        self.assertEqual(result, expected_payload)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """"""
    def test_memoize():
        """"""
        class TestClass:
            """"""
            @patch
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
