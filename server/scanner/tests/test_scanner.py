
from scanner.scanner import Scanner

from mock import Mock
from mock import patch

from unittest import TestCase


class ScannerTestCase(TestCase):

    def setUp(self):
        self.servers = [Mock(), Mock()]
        self.scanner = Scanner(servers=self.servers)

    @patch('scanner.api.user.add_user')
    def test_block_add(self, add_user):
        self.scanner.add_user('mike', 'test')
        self.assertFalse(add_user.called)

    @patch('scanner.api.user.add_user')
    def test_unblock_add(self, add_user):
        scanner = Scanner(servers=self.servers, add_users=True)
        scanner.add_user('mike', 'test')
        add_user.assert_called_once_with('mike', 'test')

    @patch('scanner.api.user.remove_user')
    def test_block_remove(self, remove_user):
        self.scanner.remove_user('mike', 'test')
        self.assertFalse(remove_user.called)

    @patch('scanner.api.user.remove_user')
    def test_unblock_remove(self, remove_user):
        scanner = Scanner(servers=self.servers, remove_users=True)
        scanner.add_user('mike', 'test')
        remove_user.assert_called_once_with('mike', 'test')


