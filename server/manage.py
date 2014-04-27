
import pprint

from crontab import CronTab

from flask.ext.script import Manager
from flask.ext.script import Server

from main import app

manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0', port=5000))

#TODO: This probably needs to be a setting somewhere. Most likely kept in the database.
VINZ_USER = 'vagrant'
VINZ_COMMENT = 'vinz'
SCAN_COMMAND = '/usr/bin/python /vagrant/server/manage.py scan'


DEV_SERVERS = {
    'ubuntu 8.04': 'vinz-ubuntu-08-04.student.iastate.edu',
    # 'ubuntu 10.04': 'vinz-ubuntu-10-04.student.iastate.edu',
    'ubuntu 12.04': 'vinz-ubuntu-12-04.student.iastate.edu',
    'debian 7': 'vinz-debian-7.student.iastate.edu',
    # 'debian 6': 'vinz-debian-6.student.iastate.edu',
    'debian 5': 'vinz-debian-5.student.iastate.edu',
    # 'debian 4': 'vinz-debian-4.student.iastate.edu',
    'fedora': 'vinz-fedora.student.iastate.edu',
    'opensuse': 'vinz-opensuse.student.iastate.edu',
    'centos': 'vinz-centos.student.iastate.edu',
}

DEV_USERS = {
    'test@test.com': ['Test', 'Tester', 'test', 'testpassword'],
    'vinz@test.com': ['Vinz', 'Vinzer', 'vinz', 'vinz'],
    'maxpete@iastate.edu': ['Max', 'Peterson', 'max', 'vinz'],
    'mpdavis@iastate.edu': ['Michael', 'Davis', 'mpdavis', 'vinz'],
    'jhummel@iastate.edu': ['Jake', 'Hummel', 'jhummel', 'vinz'],
    'zheilman@iastate.edu': ['Zach', 'Heilman', 'zheilman', 'vinz'],
}

VINZ_PUBLIC_KEY = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCrFNYehGLTslKj+YBUv4Uo2Gb2QB2IvnkTUY6JbEpl0USrObi8q+kWuV5Yhk+eUszxqu4vIIkFw1B3UK8CH76W5Fu3pcFXhBpui0h/IvDHLePmddFfx/kptdZ0qCs0VxrZgltpjCD8PtWx5nde10xYLI6V/j6yFLao/flB0qt0SJxoIbUdI0Zk99TzOmR4A5yGdW158Nvcsd+bwXshHfmjn3uafksjdSnlcqyNClo1oR3pUJKX9dQuyLA6hlGzF5/f2Sf+eggOkpLcvY7/yStfQMFF6uLZq9DHQAlXsEVnFOmHBGqoFcRKNmV2I7kcJL9QMVxWJrNIkLjBmyxACCsf example@getvinz.com'


@manager.command
def setup_dev():
    from internal import server as internal_server
    from internal import user as internal_user
    from internal import public_key as internal_public_key
    from internal.exceptions import ServerAlreadyExistsError
    from internal.exceptions import UserAlreadyExistsError

    system_user = internal_user.create_user(None, "Vinz", "System", "system@vinz.com",
                                            "vinz", "vinz")

    servers = []
    for name, url in DEV_SERVERS.iteritems():
        try:
            server = internal_server.create_server(system_user, name, url)
            servers.append(server)
            print "Created server %s: %s" % (name, url)
        except ServerAlreadyExistsError:
            print "Server %s already exists" % name
            server = internal_server.get_server_by_hostname(url)
            servers.append(server)

    for email, data in DEV_USERS.iteritems():
        user = None
        try:
            user = internal_user.create_user(system_user, data[0], data[1], email, data[2], data[3])
            print "Created user %s: %s" % (data[2], email)
        except UserAlreadyExistsError:
            user = internal_user.get_user_by_email(email)
            print "User %s already exists" % (data[2])

        if user:
            for server in servers:
                print "Adding %s to %s" % (user.username, server.hostname)
                internal_server.add_user_to_server(system_user, server, user.id)

            if not user.key_list:
                print "Adding public key for %s" % user.username
                key = internal_public_key.create_public_key(user, user, 'test key', VINZ_PUBLIC_KEY)


@manager.command
def setup_cron():
    """
    Sets up a cron job in the user's crontab in order to run the scan every minute.
    """
    cron = CronTab(user=VINZ_USER)
    num_jobs = sum(1 for _ in cron.find_comment(VINZ_COMMENT))
    if not num_jobs:
        job = cron.new(command=SCAN_COMMAND, comment=VINZ_COMMENT)
        job.minute.every(1)
        job.enable()
        cron.write()


@manager.command
def get_users():
    from scanner.api import user
    print user.get_users_on_host('vinz-debian-7.student.iastate.edu')
    print user.get_users_on_host('vinz-fedora.student.iastate.edu')
    print user.get_users_on_host('vinz-opensuse.student.iastate.edu')
    print user.get_users_on_host('vinz-centos.student.iastate.edu')


@manager.command
def add_user(username):
    from scanner.api import user
    user.add_user(username, ['vinz-ubuntu-12-04.student.iastate.edu'])


@manager.command
def remove_user(username):
    from scanner.api import user
    user.remove_user(username, ['vinz-ubuntu-12-04.student.iastate.edu'])


@manager.command
def get_keys():
    from scanner.api import ssh_key
    print ssh_key.get_authorized_keys_for_host('vinz-debian.student.iastate.edu', ['root', 'vinz', 'michael'])


@manager.command
def add_public_key(username, filename):
    from scanner.api import ssh_key
    host = 'vinz-ubuntu-12-04.student.iastate.edu'
    with open(filename) as f:
        result = ssh_key.add_user_public_key(username, [host], f.read())
    if result[host]['success']:
        print 'Successfully added key for user %s to host %s' % (username, host)
    else:
        print 'FAIL: %s' % (result[host]['error'])


@manager.command
def remove_public_key(username, filename):
    from scanner.api import ssh_key
    host = 'vinz-ubuntu-12-04.student.iastate.edu'
    with open(filename) as f:
        result = ssh_key.remove_user_public_key(username, [host], f.read())
    if result[host]['success']:
        print 'Successfully added key for user %s to host %s' % (username, host)
    else:
        print 'FAIL: %s' % (result[host]['error'])


@manager.command
def scan():
    from scanner.scanner import Scanner
    s = Scanner(debug=False, add_users=True, remove_users=True, add_keys=True, remove_keys=True)
    results = s.scan()

@manager.command
def debug_scan():
    from scanner.scanner import Scanner
    s = Scanner(debug=True, add_users=True, remove_users=True, add_keys=True, remove_keys=True)
    results = s.scan()

if __name__ == "__main__":
    manager.run()
