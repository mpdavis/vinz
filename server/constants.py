"""
.. module:: constants
   :synopsis: Location for global constants to be defined

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""


class HTTP_STATUS(object):
    SUCCESS = 200
    CREATED = 201
    ACCEPTED = 202
    DELETED = 204
    REDIRECT = 303
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    TEAPOT = 418
    ENHANCE_YOUR_CALM = 420
    SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
