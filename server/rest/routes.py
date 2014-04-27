"""
.. module:: rest.routes
   :synopsis: Location for all rest url endpoint definitions

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from rest.activity_log import ActivityLogResourceList

from rest.public_key import PublicKeyResource
from rest.public_key import PublicKeyResourceList

from rest.server import ServerResource
from rest.server import ServerResourceList
from rest.server import ServerUserGroupResource
from rest.server import ServerUserGroupResourceList
from rest.server import ServerUserResource
from rest.server import ServerUserResourceList

from rest.server_group import ServerGroupResource
from rest.server_group import ServerGroupResourceList
from rest.server_group import ServerGroupServersResource
from rest.server_group import ServerGroupServersResourceList

from rest.stats import StatisticsResource

from rest.user import UserResource
from rest.user import UserResourceList

from rest.user_group import UserGroupResource
from rest.user_group import UserGroupResourceList
from rest.user_group import UserGroupUsersResource
from rest.user_group import UserGroupUsersResourceList


BASE_API_PATH = '/api%s'


def initialize_routes(api):
    """
    Sets up all of our REST API routes.
    """

    def add_resource(path, resource, *args, **kwargs):
        """
        In order to keep all the urls lined up in a nice "column" so that they are easy to read and
        compare, I've created a wrapper for api.add_resource that reverses the first two args.
        """
        api.add_resource(resource, path, *args, **kwargs)

    # List Routes here
    add_resource(BASE_API_PATH % '/logs/', ActivityLogResourceList, endpoint='logs')

    add_resource(BASE_API_PATH % '/keys/', PublicKeyResourceList, endpoint='keys')
    add_resource(BASE_API_PATH % '/keys/<string:pub_key_id>', PublicKeyResource, endpoint='key')

    add_resource(BASE_API_PATH % '/servers/', ServerResourceList, endpoint='servers')
    add_resource(BASE_API_PATH % '/servers/<string:server_id>', ServerResource, endpoint='server')
    add_resource(BASE_API_PATH % '/servers/<string:server_id>/users/', ServerUserResourceList, endpoint='server-users')
    add_resource(BASE_API_PATH % '/servers/<string:server_id>/users/<string:user_id>', ServerUserResource, endpoint='server-user')
    add_resource(BASE_API_PATH % '/servers/<string:server_id>/usergroups/', ServerUserGroupResourceList, endpoint='server-user-groups')
    add_resource(BASE_API_PATH % '/servers/<string:server_id>/usergroups/<string:user_group_id>', ServerUserGroupResource, endpoint='server-user-group')

    add_resource(BASE_API_PATH % '/servergroups/', ServerGroupResourceList, endpoint='server-groups')
    add_resource(BASE_API_PATH % '/servergroups/<string:server_group_id>', ServerGroupResource, endpoint='server-group')
    add_resource(BASE_API_PATH % '/servergroups/<string:server_group_id>/servers/', ServerGroupServersResourceList, endpoint='server-group-servers')
    add_resource(BASE_API_PATH % '/servergroups/<string:server_group_id>/servers/<string:server_id>', ServerGroupServersResource, endpoint='server-group-server')

    add_resource(BASE_API_PATH % '/stats/', StatisticsResource, endpoint='stats')

    add_resource(BASE_API_PATH % '/users/', UserResourceList, endpoint='users')
    add_resource(BASE_API_PATH % '/users/<string:user_id>', UserResource, endpoint='user')

    add_resource(BASE_API_PATH % '/usergroups/', UserGroupResourceList, endpoint='user-groups')
    add_resource(BASE_API_PATH % '/usergroups/<string:user_group_id>', UserGroupResource, endpoint='user-group')
    add_resource(BASE_API_PATH % '/usergroups/<string:user_group_id>/users/', UserGroupUsersResourceList, endpoint='user-group-users')
    add_resource(BASE_API_PATH % '/usergroups/<string:user_group_id>/users/<string:user_id>', UserGroupUsersResource, endpoint='user-group-user')
