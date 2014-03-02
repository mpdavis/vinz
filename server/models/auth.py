"""
.. module:: models.auth
   :synopsis: Database models relating to authentication

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from mongoengine import DateTimeField
from mongoengine import Document
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import StringField

from models.audit import AuditableMixin


class User(Document, AuditableMixin):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    username = StringField(required=True)
    key_list = ListField()

    def get_display_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class UserGroup(Document, AuditableMixin):
    name = StringField(required=True)
    user_list = ListField(ReferenceField(User))


class PublicKey(Document, AuditableMixin):
    owner = ReferenceField(User)
    value = StringField(required=True)
    expire_date = DateTimeField()
