#!/usr/bin/env python3
"""models/todo.py"""
from models.base_model import BaseModel

class Todo(BaseModel):
    """This defines each todo items in our application"""
    
    def __str__(self):
        """A string representation for todo lists"""
        complete = '[+]' if self.complete == True else '[ ]'
        title = self.title
        time = self.created_at.strftime("[%H:%M %d/%m/%Y]")
        todo_id = self.id.split('-')

        return "{}  {}\t[{}]\t{}".format(complete, title, todo_id[1], time)
