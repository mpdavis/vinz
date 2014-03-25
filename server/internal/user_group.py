"""
.. module:: internal.user_group
   :synopsis: Location for internal API functions relating to UserGroup resources

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from models.auth import UserGroup


def get_user_group(group_id):
    return UserGroup.objects.get(id=group_id)
