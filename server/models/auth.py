"""
.. module:: models.auth
   :synopsis: Database models relating to authentication

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
from passlib.hash import bcrypt

from mongoengine import BooleanField
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
    password = StringField(required=True)
    username = StringField(required=True)
    active = BooleanField(required=True, default=True)
    key_list = ListField(ReferenceField('PublicKey'))

    def get_display_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @classmethod
    def encode_password(cls, raw_password):
        return bcrypt.encrypt(raw_password)

    def check_password(self, raw_password):
        return bcrypt.verify(raw_password, self.password)

    def is_active(self):
        return self.active

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    @property
    def name(self):
        return self.username


class UserGroup(Document, AuditableMixin):
    name = StringField(required=True)
    user_list = ListField(ReferenceField(User))

    def get_users(self):
        return set(self.user_list)


class PublicKey(Document, AuditableMixin):
    owner = ReferenceField(User)
    key_name = StringField(required=True)
    username = StringField(required=False)
    value = StringField(required=True)
    expire_date = DateTimeField()

    @property
    def name(self):
        return self.key_name
