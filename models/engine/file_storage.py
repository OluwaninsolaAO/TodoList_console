#!/usr/bin/env python3
"""models/engine/file_storge.py"""
import json


class FileStorage:
    """This is a storage engine for the todo
    console, using FileStorage Engine"""

    __file_path = 'file_storage.json'
    __objects = {}

    def all(self, cls=None):
        """Returns all objects in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            objs = {}
            for key, obj in FileStorage.__objects.items():
                if obj.__class__ == cls:
                    objs.update({key: obj})
            return objs

    def add(self, obj):
        """Add a new object in storage"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects.update({key: obj})

    def delete(self, obj):
        """Deletes obj in storage"""
        key = obj.__class__.__name__ + '.' + obj.id
        del FileStorage.__objects[key]

    def save(self):
        """Save objs in storage to a file storage"""
        with open(FileStorage.__file_path, 'w') as file:
            objs = {}
            for key, obj in FileStorage.__objects.items():
                objs.update({key: obj.to_dict()})
            json.dump(objs, file)

    def reload(self):
        """Reload objs from file storage to storage"""
        from models.todo import Todo
        from models.base_model import BaseModel

        class_dict = {'Todo': Todo, 'BaseModel': BaseModel}

        try:
            with open(FileStorage.__file_path, 'r') as file:
                loads = json.loads(file.read())
                objs = {}
                for key, value in loads.items():
                    objs.update({key: class_dict[value['__class__']](**value)})
                FileStorage.__objects = objs
        except FileNotFoundError:
            pass
