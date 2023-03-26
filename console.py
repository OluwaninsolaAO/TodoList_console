#!/usr/bin/env python3
"""
App: TODOList Console
DBStorage: sqllite
"""
import cmd
from models import storage
from models.todo import Todo
from datetime import datetime

class TodoList(cmd.Cmd):
    """This represents the console for our todolist app"""
    prompt = 'TodoList >> '
    intro = "Welcome to TodoList (the console):\n"

    def do_add(self, line):
        """
        Add a new todo (see also: create)
        Usage: add <title>
        """
        TodoList.add(line)

    def do_create(self, line):
        """
        Create a new todo (see also: add)
        Usage: create <title>
        """
        TodoList.add(line)

    def add(line):
        """ Add a new todo """
        if line == '':
            print("*** <title> cannot be empty!")
            return
        new = Todo()
        new.title = line
        new.complete = False
        new.save()
        print("### List updated!")

    def do_all(self, line):
        """
        List all Todo lists.
        Usage: all
        """
        if len(storage.all()) == 0:
            print("*** Nothing to see here!")
            return
        for key, todo in storage.all().items():
            print(todo)

    def do_mark(self, line):
        """
        Mark a given todo as done.
        Usage: mark <id>"""
        TodoList.mark(line)
    
    def do_done(self, line):
        """Mark a given todo as done
        Usage: done <id>"""
        TodoList.mark(line)

    def mark(line):
        """Mark a given todo as done"""
        if line == "":
            print('*** <id> cannot be empty!')
        else:
            line = line.split(' ')
            for key, todo in storage.all().items():
                todo_id = todo.id.split('-')
                if todo_id[1] in line:
                    todo.complete = True
            storage.save()
            print('### [{}] marked as complete!'.format('] ['.join(line)))

    def do_delete(self, line):
        """
        Delete todo from list.
        Usage: delete <id>
        """
        TodoList.delete(line)

    def do_destroy(self, line):
        """
        Destroy todo from list.
        Usage: destroy <id>
        """
        TodoList.delete(line)

    def delete(line):
        """
        Delete todo from list.
        """
        if line == "":
            print('*** <id> cannot be empty!')
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
            print('### [{}] deleted!'.format('] ['.join(line)))

    def do_update(self, line):
        """
        Updates the title of a todo list.
        Usage: update <id> <new title>
        """
        if line == '' or len(line.split(' ')) == 1:
            print("*** <id> or <new title> cannot be empty!")
            return
        line = line.split(' ')
        for key, obj in storage.all().items():
            if obj.id.split('-')[1] == line[0]:
                obj.title = ' '.join(line[1:])
                obj.updated_at = datetime.utcnow()
                obj.save()
                print("### Title Updated for: [{}]".format(line[0]))
                return
        print("*** <id> not valid!")

    def do_quit(self, line):
        """Quit the console"""
        return True

    def do_EOF(self, line):
        """Quit the console"""
        print()
        return True


if __name__ == '__main__':
    TodoList().cmdloop()
