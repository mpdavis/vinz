"""
.. module:: internal.user
   :synopsis: Location for internal API functions relating to user resources
"""
from internal import activity_log

from internal.exceptions import UserGroupAlreadyExistsError

from models.auth import UserGroup


def create_user_group(operator, name, **kwargs):
    """
    Create a new User Group in the database with the given values.
    """
    existing_user_group = maybe_get_user_group_by_name(name)
    if existing_user_group:
        raise UserGroupAlreadyExistsError("A usergroup with that name already exists.")
    user_group = UserGroup(name=name, lowercase_name=name.lower())
    activity_log.log_user_group_created(user_group, operator)
    user_group.save()
    return user_group


def get_user_group(user_group_id):
    """
    Fetch a single UserGroup object by its id
    :param user_group_id: The id of the UserGroup to get
    :return: The UserGroup object
    """
    return UserGroup.objects.get(id=user_group_id)


def maybe_get_user_group_by_name(user_group_name):
    """
    Tries to find a UserGroup with the given name, and returns one if it exists
    :param user_group_name: The name to lookup
    :return: A UserGroup if one exists, otherwise None
    """
    try:
        return UserGroup.objects.get(name=user_group_name)
    except UserGroup.DoesNotExist:
        return None


def get_user_groups(limit=20, offset=0, term=None):
    """
    Get a list of all UserGroups
    """
    if term:
        return list(UserGroup.objects.filter(lowercase_name__contains=term)
                                     .skip(offset).limit(limit))
    return list(UserGroup.objects.skip(offset).limit(limit))


def delete_user_group(operator, user_group_id):
    """
    Delete a UserGroup
    :param operator: The person performing this action
    :param user_group_id: The id of the UserGroup to delete
    """
    #TODO Some kind of security checks?
    user_group = get_user_group(user_group_id)
    activity_log.log_user_group_deleted(user_group, operator)
    user_group.delete()


def add_user_to_user_group(operator, user, user_group):
    """
    Add a user to a UserGroup
    :param operator: The User performing this action
    :param user: The user to add
    :param user_group: The UserGroup to add the user to
    :return: The UserGroup
    """
    if not user:
        raise ValueError("User cannot be None.")

    if not user_group:
        raise ValueError("UserGroup cannot be None.")

    if user not in user_group.user_list:
        user_group.user_list.append(user)
        user_group.save()
        activity_log.log_user_added_to_user_group(user, user_group, operator)

    return user_group


def remove_user_from_user_group(operator, user, user_group):
    """
    Remove a user to a UserGroup
    :param operator: The User performing this action
    :param user: The user to remove
    :param user_group: The UserGroup to remove the user from
    :return: The UserGroup
    """
    if not user:
        raise ValueError("User cannot be None.")

    if not user_group:
        raise ValueError("UserGroup cannot be None.")

    if user in user_group.user_list:
        user_group.user_list.remove(user)
        user_group.save()
        activity_log.log_user_removed_from_user_group(user, user_group, operator)


def get_num_user_groups():
    return UserGroup.objects.all().count()
