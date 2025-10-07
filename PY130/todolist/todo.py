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