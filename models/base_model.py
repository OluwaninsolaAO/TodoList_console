#!/usr/bin/env python3
"""models/base_model.py"""
from uuid import uuid4
from datetime import datetime


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
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """string representation"""
        return "[{}] <{}> {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def to_dict(self):
        """Returns a dictionary representation of the class
        instance using the format below:
        {<cls>.<id>:{<cls>, <dict>}"""
        obj = {}
        obj.update(self.__dict__)
        obj.update({'__class__':self.__class__.__name__})
        key = self.__class__.__name__ + '.' + self.id
        return {key: obj}

