
"""
.. module:: internal.user
   :synopsis: Location for internal API functions relating to user resources
"""
from internal.auth.utils import maybe_get_user_by_email

from internal.exceptions import UserGroupAlreadyExistsError

from models.auth import UserGroup


def create_user_group(name, **kwargs):
    """
    Create a new User Group in the database with the given values.
    """
    # TODO Auditable stuff
    existing_user_group = get_user_group_by_name(name)
    if existing_user_group:
        raise UserGroupAlreadyExistsError("A user with that email address exists.")
    user_group = UserGroup(name=name)
    user_group.save()
    return user_group


def get_user_group(user_group_id):
    return UserGroup.objects.get(id=user_group_id)

def get_user_group_by_name(user_group_name):
    try:
        return UserGroup.objects.get(name=user_group_name)
    except UserGroup.DoesNotExist:
        return None

def get_user_groups():
    # fails if requesting user is not admin
    return list(UserGroup.objects.all())

def delete_user_group(user_id):
    #TODO Some kind of security checks?
    user_group = get_user_group(user_id)
    user_group.delete()

def add_remove_check(email, user_group_name):
    """
    Check if the user is existed in a given server group
    """
    user = maybe_get_user_by_email(email)
    user_group = get_user_group_by_name(user_group_name)

    users = user_group.get_users()

    if user in users:
        return True
    else:
        return False


def add_user_to_user_group(email, user_group_name):

    user = maybe_get_user_by_email(email)
    if not user:
        raise ValueError("No user found for email: %s" % email)

    user_group = get_user_group_by_name(user_group_name)
    if not user_group:
        raise ValueError("No user group found for name: %s" % user_group_name)

    if add_remove_check(email, user_group_name) == False:
        #not sure if this is correct?
        user_group.user_list.add(user)
    else:
         print("The user: %s is already in the user group: %s" % (email, user_group_name))


def remove_user_from_user_group(email, user_group_name):
    user = maybe_get_user_by_email(email)
    if not user:
        raise ValueError("No user found for email: %s" % email)

    user_group = get_user_group_by_name(user_group_name)
    if not user_group:
        raise ValueError("No user group found for name: %s" % user_group_name)

    if add_remove_check(email, user_group_name):
        #not sure if this is correct?
        user_group.user_list.remove(user)
    else:
        print("The user: %s is not found in the user group: %s" % (email, user_group_name))
