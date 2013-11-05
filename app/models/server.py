"""
.. module:: models.server
   :synopsis: Database models relating to servers

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from app import db

from app.models.audit import AuditableMixin
from app.models.auth import PublicKey


class Server(db.Document, AuditableMixin):
    name = db.StringField(required=True)
    hostname = db.StringField(required=True)
    key_list = db.ListField(db.ReferenceField(PublicKey))


class ServerGroup(db.Document, AuditableMixin):
    name = db.StringField(required=True)
    server_list = db.ListField(db.ReferenceField(Server))
