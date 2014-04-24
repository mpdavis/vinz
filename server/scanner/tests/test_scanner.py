
from multiprocessing import Queue

from scanner.scanner import Scanner
from scanner.scanner import ServerScanner

from mock import Mock
from mock import patch

from unittest import TestCase


class ServerScannerTestCase(TestCase):

    def setUp(self):
        self.server = Mock()
        self.queue = Queue()
        self.scanner = ServerScanner(self.queue, server=self.server)

    @patch('scanner.api.user.add_user')
    def test_block_add(self, add_user):
        self.scanner.add_user('mike')
        self.assertFalse(add_user.called)

    @patch('scanner.api.user.add_user')
    def test_unblock_add(self, add_user):
        scanner = ServerScanner(queue=self.queue, server=self.server, add_users=True)
        scanner.add_user('mike')
        add_user.assert_called_once_with('mike', self.server.hostname)

    @patch('scanner.api.user.remove_user')
    def test_block_remove(self, remove_user):
        self.scanner.remove_user('mike')
        self.assertFalse(remove_user.called)

    @patch('scanner.api.user.remove_user')
    def test_unblock_remove(self, remove_user):
        scanner = ServerScanner(queue=self.queue, server=self.server, remove_users=True)
        scanner.remove_user('mike')
        remove_user.assert_called_once_with('mike', self.server.hostname)
