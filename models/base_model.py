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
            self.id = uuid4()
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
