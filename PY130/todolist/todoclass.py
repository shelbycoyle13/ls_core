class Todo:
    COMPLETE = "X"
    INCOMPLETE = " "

    def __init__(self, title):
        self._title = title
        self._done = False

    @property
    def title(self):
        return self._title
        
    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, new_value):
        self._done = new_value

    def __str__(self):
        if self._done is False:
            return f"[{Todo.INCOMPLETE}] {self._title}"
        else:
            return f"[{Todo.COMPLETE}] {self._title}"
    
    def __eq__(self, other):
        return self._done == other._done and self._title == other._title

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title
    
    def add(self, other):
        if not isinstance(other, Todo):
            raise TypeError("The object you want to add isn't a Todo object")
        self._todos.append(other)

    def __str__(self):
       output_lines = [f"---- {self._title} -----"]
       output_lines += [str(item) for item in self._todos]
       return "\n".join(output_lines)
    
    def __len__(self):
        return len(self._todos)
    
    def first(self):
        if len(self._todos) == 0:
            raise IndexError("No length, you have an empty list")
        return self._todos[0]

    def last(self):
        if len(self._todos) == 0:
            raise IndexError("No length, you have an empty list")
        return self._todos[-1]
        
    def to_list(self):
        return list(self._todos)
    
    def todo_at(self, index):
        return self._todos[index]
    
    def mark_done_at(self, index):
        self._todos[index].done = True

    def mark_undone_at(self, index):
        self._todos[index].done = False

    def mark_all_done(self):
        def mark_done(todo): #Simply marks done using assignment
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False

        self.each(mark_undone)

    def all_done(self):
        if len(self._todos) == 0:
            return True
        return all(item.done for item in self._todos)
    
    def remove_at(self, index):
        self._todos.pop(index)

    #Applies an action on each todo in the list
    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    #Returns a new TodoList containing todos that match the given condition (callback)
    def select(self, callback):
        new_list = TodoList(self.title)
        for todo in self._todos:
            if callback(todo):
                new_list.add(todo)
        
        return new_list

    #Returns the first matching todo by title
    def find_by_title(self, string):
        filtered_list = self.select(lambda todo: todo.title == string)

        if not filtered_list._todos:
            raise IndexError("No matching todos are found")
        else:
            return filtered_list._todos[0]
        
    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    #Marks done by the title of the todo
    def mark_done(self, string):
        found = self.find_by_title(string)
        found.done = True
            

empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list


# def step_1():
#     print('--------------------------------- Step 1')
#     todo_list = setup()

#     # setup() uses `todo_list.add` to add 3 todos

#     try:
#         todo_list.add(1)
#     except TypeError:
#         print('TypeError detected')    # TypeError detected

#     for todo in todo_list._todos:
#         print(todo)

# step_1()

# def step_2():
#     print('--------------------------------- Step 2')
#     todo_list = setup()

#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym

# step_2()

# def step_3():
#     print('--------------------------------- Step 3')
#     todo_list = setup()

#     print(len(todo_list))              # 3
#     print(len(empty_todo_list))        # 0

# step_3()

# def step_4():
#     print('--------------------------------- Step 4')
#     todo_list = setup()

#     print(todo_list.first())           # [ ] Buy milk
#     print(todo_list.last())            # [ ] Go to gym

#     try:
#         empty_todo_list.first()
#     except IndexError:
#         print('Expected IndexError: Got it!')

#     try:
#         empty_todo_list.last()
#     except IndexError:
#         print('Expected IndexError: Got it!')

# step_4()

# def step_5():
#     print('--------------------------------- Step 5')
#     todo_list = setup()

#     print(empty_todo_list.to_list())    # []

#     todos = todo_list.to_list()
#     print(type(todos).__name__)         # list

#     for todo in todos:
#         print(todo)                     # [ ] Buy milk
#                                         # [X] Clean room
#                                         # [ ] Go to gym

# step_5()

# def step_6():
#     print('--------------------------------- Step 6')
#     todo_list = setup()

#     print(todo_list.todo_at(0))        # [ ] Buy milk
#     print(todo_list.todo_at(1))        # [X] Clean room
#     print(todo_list.todo_at(2))        # [ ] Go to gym

#     try:
#         todo_list.todo_at(3)
#     except IndexError:
#         print('Expected IndexError: Got it!')

#     # Ensure we have a reference
#     print(todo_list.todo_at(1) is todo_list.todo_at(1))  # True

# step_6()

# def step_7():
#     print('--------------------------------- Step 7')
#     todo_list = setup()

#     todo_list.mark_done_at(0)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [X] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym

#     todo_list.mark_done_at(1)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [X] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym

#     todo_list.mark_done_at(2)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [X] Buy milk
#     # [X] Clean room
#     # [X] Go to gym

#     try:
#         todo_list.mark_done_at(3)
#     except IndexError:
#         print('Expected IndexError: Got it!')

#     todo_list.mark_undone_at(0)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [X] Go to gym

#     todo_list.mark_undone_at(1)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Clean room
#     # [X] Go to gym

#     todo_list.mark_undone_at(2)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Clean room
#     # [ ] Go to gym

#     try:
#         todo_list.mark_undone_at(3)
#     except IndexError:
#         print('Expected IndexError: Got it!')

# step_7()

# def step_8():
#     print('--------------------------------- Step 8')
#     todo_list = setup()

#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym

#     todo_list.mark_all_done()
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [X] Buy milk
#     # [X] Clean room
#     # [X] Go to gym

#     todo_list.mark_all_undone()
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Clean room
#     # [ ] Go to gym

# step_8()

# def step_9():
#     print('--------------------------------- Step 9')
#     todo_list = setup()

#     print(todo_list.all_done())         # False

#     todo_list.mark_all_done()
#     print(todo_list.all_done())         # True

#     todo_list.mark_undone_at(1)
#     print(todo_list.all_done())         # False

#     print(empty_todo_list.all_done())   # True

# step_9()

# def step_10():
#     print('--------------------------------- Step 10')
#     todo_list = setup()

#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym

#     todo_list.remove_at(1)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Go to gym

#     todo_list.remove_at(1)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk

#     try:
#         todo_list.remove_at(1)
#     except IndexError:
#         print('Expected IndexError: Got it!')

#     todo_list.remove_at(0)
#     print(todo_list)
#     # ---- Today's Todos -----

# step_10()

# def step_11():
#     print('--------------------------------- Step 11')
#     todo_list = setup()

#     todo_list.mark_all_undone()
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Clean room
#     # [ ] Go to gym

#     def done_if_y_in_title(todo):
#         if 'y' in todo.title:
#             todo.done = True

#     todo_list.each(done_if_y_in_title)
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [X] Buy milk
#     # [ ] Clean room
#     # [X] Go to gym

#     todo_list.each(lambda todo: print('>>>', todo))
#     # >>> [X] Buy milk
#     # >>> [ ] Clean room
#     # >>> [X] Go to gym

# step_11()

# def step_12():
#     print('--------------------------------- Step 12')
#     todo_list = setup()

#     def y_in_title(todo):
#         return 'y' in todo.title

#     print(todo_list.select(y_in_title))
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Go to gym

#     print(todo_list.select(lambda todo: todo.done))
#     # ---- Today's Todos -----
#     # [X] Clean room

# step_12()

# def step_13():
#     print('--------------------------------- Step 13')
#     todo_list = setup()

#     todo_list.add(Todo('Clean room'))
#     print(todo_list)
#     # ---- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [ ] Go to gym
#     # [ ] Clean room

#     found = todo_list.find_by_title('Go to gym')
#     print(found)
#     # [ ] Go to gym

#     found = todo_list.find_by_title('Clean room')
#     print(found)
#     # [X] Clean room

#     try:
#         todo_list.find_by_title('Feed cat')
#     except IndexError:
#         print('Expected IndexError: Got it!')

# step_13()

# def step_14():
#     print('--------------------------------- Step 14')
#     todo_list = setup()

#     done = todo_list.done_todos()
#     print(done)
#     # ----- Today's Todos -----
#     # [X] Clean room

#     undone = todo_list.undone_todos()
#     print(undone)
#     # ----- Today's Todos -----
#     # [ ] Buy milk
#     # [ ] Go to gym

#     done = empty_todo_list.done_todos()
#     print(done)
#     # ----- Nothing Doing -----

#     undone = empty_todo_list.undone_todos()
#     print(undone)
#     # ----- Nothing Doing -----

# step_14()

# def step_15():
#     print('--------------------------------- Step 15')
#     todo_list = setup()

#     todo_list.mark_done('Go to gym')
#     print(todo_list)
#     # ----- Today's Todos -----
#     # [ ] Buy milk
#     # [X] Clean room
#     # [X] Go to gym

#     try:
#         todo_list.mark_done('Feed cat')
#     except IndexError:
#         print('Expected IndexError: Got it!')

# step_15()

# def test_todo():
#     todo1 = Todo('Buy milk')
#     todo2 = Todo('Clean room')
#     todo3 = Todo('Go to gym')
#     todo4 = Todo('Clean room')

#     print(todo1)                  # [ ] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [ ] Clean room

#     print(todo2 == todo4)         # True
#     print(todo1 == todo2)         # False
#     print(todo4.done)             # False

#     todo1.done = True
#     todo4.done = True
#     print(todo4.done)             # True

#     print(todo1)                  # [X] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [X] Clean room

#     print(todo2 == todo4)         # False

#     todo4.done = False
#     print(todo4.done)             # False
#     print(todo4)                  # [ ] Clean room

# test_todo()