"""
.. module:: models.auth
   :synopsis: Database models relating to authentication

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from app import db

from app.models.audit import AuditableMixin


class User(db.Document, AuditableMixin):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True)
    key_list = db.ListField()

    def get_display_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class UserGroup(db.Document, AuditableMixin):
    name = db.StringField(required=True)
    user_list = db.ListField(db.ReferenceField(User))


class PublicKey(db.Document, AuditableMixin):
    owner = db.ReferenceField(User)
    value = db.TextField(required=True)
    expire_date = db.DateTimeField()
