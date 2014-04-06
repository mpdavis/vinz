"""
.. module:: internal.scan_log
   :synopsis: Functions dealing with keeping track of server scans.

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
import datetime

from constants import SCAN_LOG_STATUS

from models.audit import ScanLog


def create_scan_log(server, server_status, users_expected, actual_users, unexpected_users):
    now = datetime.datetime.now()

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
        users_expected=users_expected,
        actual_users=actual_users,
        unexpected_users=unexpected_users,
    )
    log.save()
    return log
