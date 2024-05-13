#!/usr/bin/env python3
"""
test_client module has test classes
for testing the client module
"""
import unittest
from client import GithubOrgClient, get_json
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """test class"""
    @parameterized.expand([
        ('google', {'login': "google"}),
        ('abc', {'login': "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected: Dict, mock_org: MagicMock):
        """This method tests that GithubOrgClient.org
        returns the correct value."""
        mock_org.return_value = MagicMock(return_value=expected)
        self.assertEqual(GithubOrgClient(org_name).org(), expected)
        mock_org.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
