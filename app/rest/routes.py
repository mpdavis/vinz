"""
.. module:: rest.routes
   :synopsis: Location for all rest url endpoint definitions

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from app.rest.server import ServerResource
from app.rest.server import ServerResourceList


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
    add_resource(BASE_API_PATH % '/servers/', ServerResourceList)
    add_resource(BASE_API_PATH % '/servers/<string:server_id>', ServerResource)
