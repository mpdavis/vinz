
from mock import Mock
from mock import patch

from unittest import TestCase

from scanner.api import ssh_key as api_ssh_key
from scanner.runner import VinzRunner


EXAMPLE_CORRECT_RETURN_VALUE = {
    'dark': {},
    'contacted': {
        'vinz-ubuntu.student.iastate.edu': {
            'changed': True,
            'end': '2014-03-23 16:58:23.763850',
            'stdout': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBffoYSqLvMeUOLcKXkeen7wj/t9rwtaKGJ3Mjq//8Zfl5kBrqV2JqT3BoNGFgjHm1Hrzk1873kOcajK/b/8mQahx77LDMT7Mi4gvoVJ7/U2u6LCI7tLeqSqgI7GJFRdz3RpsCz6iUOp5j5eGvLO4g8YE+P0WByCgv6hajsi+2f6zdPuQdcckHj8GO/Tpf1uIcibiUfAqzkTshhJFfI0oZg/ba2Q5O8iLCO9DBTO9aQg26LiEE53/d9nHlvwAv9ER94ZPjXpNj1vV+HWN2cK+I0ZO2UBjUIDbMXLId5yNEzsKpyhoKso/ThELk95dzQkKzPBicRYCiVWoFLJlnmLOx mike.philip.davis@gmail.com\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCrFNYehGLTslKj+YBUv4Uo2Gb2QB2IvnkTUY6JbEpl0USrObi8q+kWuV5Yhk+eUszxqu4vIIkFw1B3UK8CH76W5Fu3pcFXhBpui0h/IvDHLePmddFfx/kptdZ0qCs0VxrZgltpjCD8PtWx5nde10xYLI6V/j6yFLao/flB0qt0SJxoIbUdI0Zk99TzOmR4A5yGdW158Nvcsd+bwXshHfmjn3uafksjdSnlcqyNClo1oR3pUJKX9dQuyLA6hlGzF5/f2Sf+eggOkpLcvY7/yStfQMFF6uLZq9DHQAlXsEVnFOmHBGqoFcRKNmV2I7kcJL9QMVxWJrNIkLjBmyxACCsf /home/vagrant/.ssh/id_rsa',
            'cmd': ['cat', '~vinz/.ssh/authorized_keys'],
            'rc': 0,
            'start': '2014-03-23 16:58:23.754514',
            'stderr': '',
            'delta': '0:00:00.009336',
            'invocation': {
                'module_name': 'command',
                'module_args': 'cat ~vinz/.ssh/authorized_keys'
            }
        }
    }
}


CORRECT_OUTPUT = {
    'vinz': [
        u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBffoYSqLvMeUOLcKXkeen7wj/t9rwtaKGJ3Mjq//8Zfl5kBrqV2JqT3BoNGFgjHm1Hrzk1873kOcajK/b/8mQahx77LDMT7Mi4gvoVJ7/U2u6LCI7tLeqSqgI7GJFRdz3RpsCz6iUOp5j5eGvLO4g8YE+P0WByCgv6hajsi+2f6zdPuQdcckHj8GO/Tpf1uIcibiUfAqzkTshhJFfI0oZg/ba2Q5O8iLCO9DBTO9aQg26LiEE53/d9nHlvwAv9ER94ZPjXpNj1vV+HWN2cK+I0ZO2UBjUIDbMXLId5yNEzsKpyhoKso/ThELk95dzQkKzPBicRYCiVWoFLJlnmLOx mike.philip.davis@gmail.com',
        u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCrFNYehGLTslKj+YBUv4Uo2Gb2QB2IvnkTUY6JbEpl0USrObi8q+kWuV5Yhk+eUszxqu4vIIkFw1B3UK8CH76W5Fu3pcFXhBpui0h/IvDHLePmddFfx/kptdZ0qCs0VxrZgltpjCD8PtWx5nde10xYLI6V/j6yFLao/flB0qt0SJxoIbUdI0Zk99TzOmR4A5yGdW158Nvcsd+bwXshHfmjn3uafksjdSnlcqyNClo1oR3pUJKX9dQuyLA6hlGzF5/f2Sf+eggOkpLcvY7/yStfQMFF6uLZq9DHQAlXsEVnFOmHBGqoFcRKNmV2I7kcJL9QMVxWJrNIkLjBmyxACCsf /home/vagrant/.ssh/id_rsa'
    ]
}


class SSHKeyAPITestCase(TestCase):

    @patch('scanner.runner.VinzRunner.run')
    def test_get_users(self, m_run):
        m_run.return_value = EXAMPLE_CORRECT_RETURN_VALUE
        ssh_keys = api_ssh_key.get_authorized_keys_for_host('vinz-ubuntu.student.iastate.edu', ['vinz'])
        self.assertDictEqual(ssh_keys, CORRECT_OUTPUT)
