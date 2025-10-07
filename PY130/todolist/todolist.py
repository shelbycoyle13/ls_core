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