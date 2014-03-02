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
    return public_key


def get_public_key(pub_key_id):
    return PublicKey.objects.get(id=pub_key_id)


def delete_public_key(pub_key_id):
    #TODO Some kind of security checks?
    public_key = get_public_key(pub_key_id)
    public_key.delete()
