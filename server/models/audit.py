"""
.. module:: app.models.audit
   :synopsis: Place for models/collections dealing with auditing/logging

.. moduleauthor:: Max Peterson <maxpete@iastate.edu>

"""
import datetime

from mongoengine import DateTimeField
from mongoengine import Document
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
    actor = ReferenceField('User', required=True)
    timestamp = DateTimeField(default=datetime.datetime.now)
    obj = ReferenceField(Document)  # Not sure on this yet
    action = StringField()  # TODO: Define possible values for this
