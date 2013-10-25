"""
.. module:: rest.server
   :synopsis: REST Resource definitions relating to servers

.. moduleauthor:: Max Peterson <maxwell.peterson@webfilings.com>

"""
from flask.ext.restful import Resource


class ServerResource(Resource):
    """
    REST endpoint to serve up details of a specific Server from the database.
    """

    def get(self):
        return

    def put(self):
        return


class ServerResourceList(Resource):
    """
    REST endpoint to serve up a list of Server resources from the database.
    """

    def get(self):
        return

    def post(self):
        return
