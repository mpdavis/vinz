
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
    name = "%s %s" % (first_name, last_name)
    lower_name = name.lower()
    user = User(first_name=first_name, last_name=last_name, email=email, username=username,
                lowercase_display_name=lower_name)
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


def get_users(limit=20, offset=0, term=None):
    # TODO fails if requesting user is not admin
    if term:
        return list(User.objects.filter(lowercase_display_name__contains=term)
                                .skip(offset).limit(limit))
    return list(User.objects.skip(offset).limit(limit))


def get_all_users():
    return list(User.objects.all())


def delete_user(operator, user_id):
    #TODO Some kind of security checks?
    user = get_user(user_id)
    activity_log.log_user_deleted(user, operator)
    user.delete()


def get_num_users():
    return User.objects.all().count()
