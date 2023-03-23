#!/usr/bin/env python3
"""models/base_model.py"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """This class defines a generic attributes
    accross the entire application such at id,
    created_at and updated_at"""

    def __init__(self, *args, **kwargs):
        """Constructor method for the class BaseModel"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        else:
            at_list = ['created_at', 'updated_at']
            for at in at_list:
                kwargs[at] = datetime.fromisoformat(kwargs[at])
            del kwargs['__class__']
            self.__dict__.update(kwargs)

        storage.add(self)
        storage.save()

    def __str__(self):
        """string representation"""
        return "[{}] <{}> {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of the 
        class instance"""
        obj = {}
        obj.update(self.__dict__)
        obj.update({'__class__' : self.__class__.__name__})
        at_list = ['created_at', 'updated_at']
        for at in at_list:
            obj[at] = obj[at].isoformat()
        return obj

    def save(self):
        """Save all changes to storage"""
        storage.save()

    def delete(self):
        """Deletes instance from storage"""
        storage.delete(self)
        storage.save()
