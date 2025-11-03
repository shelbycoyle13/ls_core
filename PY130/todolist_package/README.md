# todolist_shelbycoyle

A simple todo list package with `Todo` and `TodoList` classes.

## Installation (TestPyPI)
```bash
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps todolist_shelbycoyle


## Usage
from todolist_shelbycoyle.todo import Todo
from todolist_shelbycoyle.todolist import TodoList

todo_list = TodoList("Today's Todos")
todo_list.add(Todo("Buy milk"))
todo_list.add(Todo("Clean room"))

print(todo_list)
# ---- Today's Todos -----
# [ ] Buy milk
# [ ] Clean room

## Requirements
Python 3.8+

## Links
Homepage = "https://github.com/shelbycoyle13/ls_core/tree/04bf2af5507b2cccf84395f4e40eee972650a2f6/PY130/todolist"
Issues = "https://github.com/shelbycoyle13/ls_core/issues"

## License

MIT License. See LICENSE file.