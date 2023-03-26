#!/usr/bin/env python3
"""
App: TODOList Console
DBStorage: sqllite
"""
import cmd
from models import storage
from models.todo import Todo

class TodoList(cmd.Cmd):
    """This represents the console for our todolist app"""
    prompt = 'TodoList >> '
    intro = "Welcome to TodoList (the console):\n"

    def do_add(self, line):
        """
        Add a new todo
        Usage: add <Todo Title>
        """
        TodoList.add(line)

    def do_create(self, line):
        """
        Create a new todo
        Usage: create <Todo Title>
        """
        TodoList.add(line)

    def add(line):
        """
        Add a new todo
        Usage: add <Todo Title>
        """
        new = Todo()
        new.title = line
        new.complete = False
        new.save()
        print("## List updated!")

    def do_all(self, line):
        """
        List all Todo lists.
        """
        for key, todo in storage.all().items():
            print(todo)

    def do_mark(self, line):
        """Mark a given todo as done"""
        TodoList.mark(line)
    
    def do_done(self, line):
        """Mark a given todo as done"""
        TodoList.mark(line)

    def mark(line):
        """Mark a given todo as done"""
        if line == "":
            print('** Please add a todo object add **')
        else:
            line = line.split(' ')
            for key, todo in storage.all().items():
                todo_id = todo.id.split('-')
                if todo_id[1] in line:
                    todo.complete = True
            storage.save()

    def do_delete(self, line):
        """
        Delete todo from list.
        """
        TodoList.delete(line)

    def do_destroy(self, line):
        """
        Destroy todo from list.
        """
        TodoList.delete(line)

    def delete(line):
        """
        Delete todo from list.
        """
        if line == "":
            print('** Please specify a todo id **')
        else:
            line = line.split(' ')
            delete_list = []
            for key, todo in storage.all().items():
                todo_id = todo.id.split('-')
                if todo_id[1] in line:
                    delete_list.append(todo)
            for todo in delete_list:
                storage.delete(todo)
            storage.save()

    def do_quit(self, line):
        """Quit the console"""
        return True

    def do_EOF(self, line):
        """Quit the console"""
        print()
        return True


if __name__ == '__main__':
    TodoList().cmdloop()
