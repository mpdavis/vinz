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
from models.auth import PublicKey


class Server(Document, AuditableMixin):
    name = StringField(required=True)
    hostname = StringField(required=True)
    key_list = ListField(ReferenceField(PublicKey))


class ServerGroup(Document, AuditableMixin):
    name = StringField(required=True)
    server_list = ListField(ReferenceField(Server))
