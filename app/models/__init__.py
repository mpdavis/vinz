"""
.. module:: 
   :synopsis: 

.. moduleauthor:: Max Peterson <maxwell.peterson@webfilings.com>

"""
import datetime

from app import db

from app.models.auth import User


class AuditableMixin(object):
    """
    Abstract class meant to be inherited alongside a Mongoengine Document.  Automatically
    sets the modified_date and creation_date.
    """
    creator = db.ReferenceField(User)
    creation_date = db.DateTimeField()
    modified_by = db.ReferenceField(User)
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(AuditableMixin, self).save(*args, **kwargs)
