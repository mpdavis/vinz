"""
.. module:: models.server
   :synopsis: Database models relating to servers

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from app import db

from app.models import AuditableMixin


class Server(db.Document, AuditableMixin):
    name = db.StringField(required=True)
    hostname = db.StringField(required=True)
    key_list = db.ListField()
