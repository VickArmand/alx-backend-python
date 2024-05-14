#!/usr/bin/env python3
"""
test_client module has test classes
for testing the client module
"""
import unittest
from client import GithubOrgClient, get_json
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """ unit-test GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mocked_org:
            mocked_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            repo_url = GithubOrgClient('google')._public_repos_url
            expected_repo = "https://api.github.com/users/google/repos"
            self.assertEqual(repo_url, expected_repo)

    @patch('client.get_json')
    def test_public_repos(self, mock_json: MagicMock) -> None:
        """unit-test GithubOrgClient.public_repos"""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_json.return_value = test_payload["repos"]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as patched_url:
            self.assertEqual(GithubOrgClient('google').public_repos(),
                             ['episodes.dart', 'kratu'])
            patched_url.assert_called_once()
        mock_json.assert_called_once()

    @parameterized.expand([
        ({"key": "my_license"}, "my_license", False),
        ({"key": "other_license"}, "my_license", False)
    ])
    def test_has_license(self,
                         repo: Dict[str, Dict],
                         license_key: str,
                         expected_has_license: bool) -> None:
        """
        unit-test GithubOrgClient.has_license.
        Parametrize the test with the following inputs
        repo={"license": {"key": "my_license"}}, license_key="my_license"
        repo={"license": {"key": "other_license"}}, license_key="my_license"
        You should also parameterize the expected returned value.
        """
        has_license = GithubOrgClient('google').has_license(repo, license_key)
        self.assertEqual(has_license, expected_has_license)
