#!/usr/bin/env python3
"""
App: TODOList Console
DBStorage: sqllite
"""
import cmd

class TodoList(cmd.Cmd):
    """This represents the console for our todolist app"""
    prompt = 'TodoList >> '


if __name__ == '__main__':
    TodoList().cmdloop()
