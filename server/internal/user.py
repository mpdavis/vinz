
"""
.. module:: internal.user
   :synopsis: Location for internal API functions relating to user resources
"""
from internal import activity_log

from internal.auth.utils import maybe_get_user_by_email

from internal.exceptions import UserAlreadyExistsError

from models.auth import User


def create_user(operator, first_name, last_name, email, username, password, **kwargs):
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
    activity_log.log_user_created(user, operator)
    return user


def get_user(user_id):
    return User.objects.get(id=user_id)


def get_user_by_username(username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None


def get_user_by_email(email):
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def get_users():
    # fails if requesting user is not admin
    return list(User.objects.all())


def delete_user(operator, user_id):
    #TODO Some kind of security checks?
    user = get_user(user_id)
    activity_log.log_user_deleted(user, operator)
    user.delete()
