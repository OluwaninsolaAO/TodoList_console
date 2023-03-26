# TodoList_console
This is a simple console-based Todo List application built using Python. The purpose of this application is to allow users to create and manage their personal to-do lists.

### Features
The following features will be added to the application:
- __Add tasks__: Users can add tasks to their to-do list by entering a task description.
- __View tasks__: Users can view their entire to-do list or a specific task.
- __Edit tasks__: Users can edit the description of an existing task.
- __Delete tasks__: Users can delete a task from their to-do list.
- __Save tasks__: Users can save their to-do list to a file, and load it again when they launch the application.

### Usage
To use the application, simply clone and run the Python script `console.py` in your console. You will be presented with a menu of options to choose from, including adding a task, viewing your to-do list, editing a task, deleting a task, and saving your to-do list.

```
$ ./console.py 
Welcome to TodoList (the console):

TodoList >> help

Documented commands (type help <topic>):
========================================
EOF  add  all  create  delete  destroy  done  help  mark  quit  update

TodoList >> add Join a bookclub
### List updated!

TodoList >> create Fix broken log
### List updated!

TodoList >> all
[ ]  Join a bookclub    [9f34]  [15:34 26/03/2023]
[ ]  Fix broken log     [36ac]  [15:34 26/03/2023]

TodoList >> mark 9f34
### [9f34] marked as complete!

TodoList >> all
[+]  Join a bookclub    [9f34]  [15:34 26/03/2023]
[ ]  Fix broken log     [36ac]  [15:34 26/03/2023]

TodoList >> delete 9f34
### [9f34] deleted!

TodoList >> all
[ ]  Fix broken log     [36ac]  [15:34 26/03/2023]

TodoList >> update 36ac Fix broken bike
### Title Updated for: [36ac]

TodoList >> all
[ ]  Fix broken bike    [36ac]  [15:34 26/03/2023]

TodoList >> 
```

### Requirements
The application requires Python 3.x to be installed on your system.

### Contributing
Contributions to the project are welcome. If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.
