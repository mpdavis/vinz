"""
.. module:: internal.public_key
   :synopsis: Location for internal API functions relating to public key resources

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>
"""
from internal import activity_log

from models.auth import PublicKey

import datetime


def create_public_key(operator, user, key_name, value, **kwargs):
    """
    Create a new user in the database with the given values.
    :param operator: User creating this PublicKey
    :param user: The User who this PublicKey belongs to
    :param key_name: The name given to this PubicKey to easily identify it
    :param value: The actual key's value
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
    activity_log.log_public_key_added(public_key, user, operator)
    user.key_list.append(public_key)
    user.save()
    return public_key


def get_public_key(pub_key_id):
    """
    Fetch a single PublicKey by id
    :param pub_key_id: The id of the PublicKey to get
    :return: The PublicKey object from the database
    """
    return PublicKey.objects.get(id=pub_key_id)


def get_user_keys(user):
    """
    Get a list of PublicKey objects for a given User
    :param user: The User to get the PublicKeys for
    :return: A list of PublicKey objects
    """
    return list(user.key_list)


def delete_public_key(operator, user, pub_key_id):
    """
    Remove a public key from all servers and delete it from the database
    :param operator: The User deleting this PublicKey
    :param user: User who the public key belongs to
    :param pub_key_id: id of the public key to remove
    """
    public_key = get_public_key(pub_key_id)
    activity_log.log_public_key_deleted(public_key, user, operator)
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
