"""
.. module:: models.server
   :synopsis: Database models relating to servers

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from mongoengine import Document
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import StringField

from models.audit import AuditableMixin
from models.auth import User
from models.auth import UserGroup


class Server(Document, AuditableMixin):
    name = StringField(required=True)
    hostname = StringField(required=True)
    user_list = ListField(ReferenceField(User))
    group_list = ListField(ReferenceField(UserGroup))


class ServerGroup(Document, AuditableMixin):
    name = StringField(required=True)
    server_list = ListField(ReferenceField(Server))
