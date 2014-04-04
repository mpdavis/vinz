"""
.. module:: internal.public_key
   :synopsis: Location for internal API functions relating to public key resources

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>
"""
from models.auth import PublicKey

import datetime


def create_public_key(user, key_name, value, **kwargs):
    """
    Create a new user in the database with the given values.
    """
    public_key = PublicKey(
        owner=user,
        username=user.username,
        key_name=key_name,
        value=value,
        # TODO Set this expire time based on some account setting.
        expire_date=datetime.datetime.now() + datetime.timedelta(days=90)
    )
    public_key.save()
    user.key_list.append(public_key)
    user.save()
    return public_key


def get_public_key(pub_key_id):
    return PublicKey.objects.get(id=pub_key_id)


def get_user_keys(user):
    return list(user.key_list)


def delete_public_key(user, pub_key_id):
    #TODO Some kind of security checks?
    public_key = get_public_key(pub_key_id)
    user.key_list.remove(public_key)
    user.save()
    public_key.delete()


def get_user_keys_for_server(server):
    """
    Get a dict of user:public_key_value for a server
    :param server: The Server object
    :return: dict
    """
    access_dict = {}
    users = server.get_all_users()
    for user in users:
        key_value_list = []
        for key in user.key_list:
            key_value_list.append(key.value)
        access_dict[user.username] = key_value_list

    return access_dict
