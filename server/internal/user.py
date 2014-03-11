
"""
.. module:: internal.user
   :synopsis: Location for internal API functions relating to user resources
"""
from internal.auth.utils import maybe_get_user_by_email

from internal.exceptions import UserAlreadyExistsError

from internal.server import maybe_get_server_by_hostname

from models.auth import User


def create_user(first_name, last_name, email, username, password, **kwargs):
    """
    Create a new user in the database with the given values.
    """
    # TODO Auditable stuff
    existing_user = maybe_get_user_by_email(email)
    if existing_user:
        raise UserAlreadyExistsError("A user with that email address exists.")
    user = User(first_name=first_name, last_name=last_name, email=email, username=username)
    user.password = User.encode_password(password)
    user.save()
    return user


def get_user(user_id):
    return User.objects.get(id=user_id)


def get_users():
    # fails if requesting user is not admin
    return list(User.objects.all())


def delete_user(user_id):
    #TODO Some kind of security checks?
    user = get_user(user_id)
    user.delete()


def get_users_for_hostname(hostname):
    server = maybe_get_server_by_hostname(hostname)
    
    if not server:
        raise ValueError("No server found for hostname: %s" % hostname)

    users = server.get_users()
    return users


def get_usernames_for_hostname(hostname):
    server = maybe_get_server_by_hostname(hostname)
    
    if not server:
        raise ValueError("No server found for hostname: %s" % hostname)

    usernames = server.get_usernames()
    return usernames
