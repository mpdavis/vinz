
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
    existing_userGroup = get_userGroup_by_name(name)
    if existing_userGroup:
        raise UserGroupAlreadyExistsError("A user with that email address exists.")
    userGroup = UserGroup(name=name)
    userGroup.save()
    return userGroup


def get_user_group(userGroup_id):
    return UserGroup.objects.get(id=userGroup_id)

def get_user_group_by_name(user_group_name):
    try:
        return UserGroup.objects.get(name=user_group_name)
    except UserGroup.DoesNotExist:
        return None

def get_user_groups():
    # fails if requesting user is not admin
    return list(UserGroup.objects.all())

def delete_userGroup(user_id):
    #TODO Some kind of security checks?
    userGroup = get_user_group(user_id)
    userGroup.delete()

def add_remove_check(email,user_group_name):
    """
    Check if the user is existed in a given server group
    """
    user = maybe_get_user_by_email(email)
    userGroup = get_user_group_by_name(user_group_name)

    users = userGroup.get_users()

    if user in users:
        return True
    else:
        return False


def add_user_to_user_group(email,user_group_name):

    user = maybe_get_user_by_email(email)
    if not user:
        raise ValueError("No user found for email: %s" % email)

    userGroup = get_user_group_by_name(user_group_name)
    if not userGroup:
        raise ValueError("No user group found for name: %s" % user_group_name)

    if add_remove_check(email,user_group_name) == False:
        #not sure if this is correct?
        userGroup.user_list.add(user)
    else:
         raise ValueError("The user: %s is already in the user group: %s" % (email, user_group_name))


def remove_user_from_user_group(email,user_group_name):
    user = maybe_get_user_by_email(email)
    if not user:
        raise ValueError("No user found for email: %s" % email)

    userGroup = get_user_group_by_name(user_group_name)
    if not userGroup:
        raise ValueError("No user group found for name: %s" % user_group_name)

    if add_remove_check(email,user_group_name) == True:
        #not sure if this is correct?
        userGroup.user_list.remove(user)
    else:
         raise ValueError("The user: %s is not found in the user group: %s" % (email, user_group_name))
