
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


@manager.command
def setup_dev():
    from internal import server
    from internal import user

    server.create_server('ubuntu', 'vinz-ubuntu.student.iastate.edu')
    server.create_server('debian', 'vinz-debian.student.iastate.edu')

    user.create_user('Test', 'Tester', 'test@test.com')


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
def scan():
    pass

if __name__ == "__main__":
    manager.run()
