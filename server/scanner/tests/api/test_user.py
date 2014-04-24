
from mock import Mock
from mock import patch

from unittest import TestCase

from scanner.api import user as api_user
from scanner.runner import VinzRunner


EXAMPLE_CORRECT_RETURN_VALUE = {
    'dark': {}, 
    'contacted': {
        'vinz-ubuntu.student.iastate.edu': {
            u'changed': True, 
            u'end': u'2014-03-11 13:26:25.880537', 
            u'stdout': u'root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/bin/sh\nbin:x:2:2:bin:/bin:/bin/sh\nsys:x:3:3:sys:/dev:/bin/sh\nsync:x:4:65534:sync:/bin:/bin/sync\ngames:x:5:60:games:/usr/games:/bin/sh\nman:x:6:12:man:/var/cache/man:/bin/sh\nlp:x:7:7:lp:/var/spool/lpd:/bin/sh\nmail:x:8:8:mail:/var/mail:/bin/sh\nnews:x:9:9:news:/var/spool/news:/bin/sh\nuucp:x:10:10:uucp:/var/spool/uucp:/bin/sh\nproxy:x:13:13:proxy:/bin:/bin/sh\nwww-data:x:33:33:www-data:/var/www:/bin/sh\nbackup:x:34:34:backup:/var/backups:/bin/sh\nlist:x:38:38:Mailing List Manager:/var/list:/bin/sh\nirc:x:39:39:ircd:/var/run/ircd:/bin/sh\ngnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh\nnobody:x:65534:65534:nobody:/nonexistent:/bin/sh\nlibuuid:x:100:101::/var/lib/libuuid:/bin/sh\nsyslog:x:101:103::/home/syslog:/bin/false\nmessagebus:x:102:105::/var/run/dbus:/bin/false\nwhoopsie:x:103:106::/nonexistent:/bin/false\nlandscape:x:104:109::/var/lib/landscape:/bin/false\nsshd:x:105:65534::/var/run/sshd:/usr/sbin/nologin\nvinz:x:1000:1000:vinz,,,:/home/vinz:/bin/bash', 
            u'cmd': [u'cat', u'/etc/passwd'], 
            u'rc': 0, 
            u'start': u'2014-03-11 13:26:25.872194', 
            u'stderr': u'', 
            u'delta': u'0:00:00.008343', 
            'invocation': {
                'module_name': 'command',
                'module_args': 'cat /etc/passwd'
            }
        }
    }
}


class UserAPITestCase(TestCase):

    @patch('scanner.runner.VinzRunner.run')
    def test_get_users(self, m_run):
        m_run.return_value = EXAMPLE_CORRECT_RETURN_VALUE
        users = api_user.get_users_on_host('vinz-ubuntu.student.iastate.edu')
        self.assertTrue('vinz' in users)

    @patch('scanner.runner.VinzRunner.run')
    def test_ignore_users(self, m_run):
        m_run.return_value = EXAMPLE_CORRECT_RETURN_VALUE
        users = api_user.get_users_on_host('vinz-ubuntu.student.iastate.edu')
        self.assertFalse('games' in users)
        self.assertFalse('daemon' in users)
        self.assertFalse('www-data' in users)
