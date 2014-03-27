
from crontab import CronTab

from flask.ext.script import Manager
from flask.ext.script import Server

from main import app

manager = Manager(app)
manager.add_command("runserver", Server(host='0.0.0.0', port=5000))

#TODO: This probably needs to be a setting somewhere. Most likely kept in the database.
VINZ_USER = 'vagrant'
VINZ_COMMENT = 'vinz'
SCAN_COMMAND = '/usr/bin/python /vagrant/app/manage.py scan'


DEV_SERVERS = {
    'ubuntu': 'vinz-ubuntu.student.iastate.edu',
    'debian': 'vinz-debian.student.iastate.edu',
}

DEV_USERS = {
    'test@test.com': ['Test', 'Tester', 'test', 'testpassword'],
    'maxpete@iastate.edu': ['Max', 'Peterson', 'maxpete', 'vinz'],
    'mpdavis@iastate.edu': ['Michael', 'Davis', 'mpdavis', 'vinz'],
}


@manager.command
def setup_dev():
    from internal import server
    from internal import user
    from internal.exceptions import ServerAlreadyExistsError
    from internal.exceptions import UserAlreadyExistsError

    for name, url in DEV_SERVERS.iteritems():
        try:
            server.create_server(name, url)
        except ServerAlreadyExistsError:
            pass

    for email, data in DEV_USERS.iteritems():
        try:
            user.create_user(data[0], data[1], email, data[2], data[3])
        except UserAlreadyExistsError:
            pass


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
    print user.get_users_on_host('vinz-ubuntu.student.iastate.edu')


@manager.command
def add_user(username):
    from scanner.api import user
    user.add_user(username, ['vinz-ubuntu.student.iastate.edu'])


@manager.command
def remove_user(username):
    from scanner.api import user
    user.remove_user(username, ['vinz-ubuntu.student.iastate.edu'])


@manager.command
def get_keys():
    from scanner.api import ssh_key
    print ssh_key.get_authorized_keys_for_host('vinz-debian.student.iastate.edu', ['root', 'vinz', 'michael'])


@manager.command
def scan():
    from scanner.scanner import Scanner
    s = Scanner()
    s.scan()


if __name__ == "__main__":
    manager.run()
