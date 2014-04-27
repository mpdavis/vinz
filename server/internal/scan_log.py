"""
.. module:: internal.scan_log
   :synopsis: Functions dealing with keeping track of server scans.

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
import datetime

from constants import SCAN_LOG_STATUS

from models.audit import ScanLog


def create_scan_log(server, server_status, users_expected=None, actual_users=None, unexpected_users=None):
    now = datetime.datetime.now()

    if not users_expected:
        users_expected = []

    if not actual_users:
        actual_users = []

    if not unexpected_users:
        unexpected_users = []

    actual_users_set = set(actual_users)
    users_expected_set = set(users_expected)

    if unexpected_users:
        status = SCAN_LOG_STATUS.EXCEPTION
    elif users_expected_set.difference(actual_users_set):
        status = SCAN_LOG_STATUS.USERS_ALTERED
    else:
        status = SCAN_LOG_STATUS.NO_CHANGE

    log = ScanLog(
        server=server,
        server_status=server_status,
        timestamp=now,
        status=status,
        users_expected=list(users_expected),
        actual_users=list(actual_users),
        unexpected_users=list(unexpected_users),
    )
    log.save()
    return log


def get_all_scan_logs(limit=20, offset=0):
    """
    Get all the activity logs in the database
    :return: A list of ActivityLog objects
    """
    return list(ScanLog.objects.skip(offset).limit(limit).order_by('-timestamp'))


def get_num_scan_logs():
    return ScanLog.objects.all().count()
