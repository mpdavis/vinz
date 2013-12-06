
"""
.. module:: internal.user
   :synopsis: Location for internal API functions relating to user resources
"""
from app.models.auth import User


def create_user(first_name, last_name, email, **kwargs):
    """
    Create a new user in the database with the given values.
    """
    # TODO Auditable stuff
    user = User(first_name=first_name, last_name=last_name,email=email)
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
