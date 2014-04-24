"""
.. module:: app.models.audit
   :synopsis: Place for models/collections dealing with auditing/logging

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
import datetime

from mongoengine import DateTimeField
from mongoengine import Document
from mongoengine import GenericReferenceField
from mongoengine import IntField
from mongoengine import ListField
from mongoengine import ReferenceField
from mongoengine import StringField


class AuditableMixin(object):
    """
    Abstract class meant to be inherited alongside a Mongoengine Document.  Automatically
    sets the modified_date and creation_date.
    """
    creator = ReferenceField('User')
    creation_date = DateTimeField()
    modified_by = ReferenceField('User')
    modified_date = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(AuditableMixin, self).save(*args, **kwargs)


class ActivityLog(Document):
    """
    Keep track of user activities
    Example: Matthew added a user "max" to server "host1"
    Example: User "max" uploaded a new public key
    """
    actor = ReferenceField('User')
    timestamp = DateTimeField(default=datetime.datetime.now)
    obj = GenericReferenceField()
    secondary_obj = GenericReferenceField(required=False)

    # Possible values defined in constants.AUDIT_ACTIONS
    action = StringField()


class ScanLog(Document):
    """
    Keep record of every scan that happens for every server
    """
    server = ReferenceField('Server', required=True)
    timestamp = DateTimeField(default=datetime.datetime.now)

    # Possible statuses defined in constants.SCAN_LOG_STATUS
    status = IntField()
    server_status = IntField()

    users_expected = ListField(StringField())
    actual_users = ListField(StringField())
    unexpected_users = ListField(StringField())
