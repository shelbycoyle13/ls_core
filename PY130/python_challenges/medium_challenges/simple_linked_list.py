class Element:
    def __init__(self, data, element_obj=None): #element_obj
        self.data = data
        self.element_obj = element_obj

    @property
    def datum(self): #We use the name datum since the tests expect us to use it. Datum is the singular of data
        return self.data

    @property
    def next(self): #Returns the "older" object
        return self.element_obj

    def is_tail(self): #Needs to return a boolean. #Checks whether we've reached the final element
        return self.next is None

class SimpleLinkedList: #These HAVE Elements
    def __init__(self):
        self._head = None #This is the default value. If there's a head, we'll return it. Returning the head actually returns an Element, since a head IS an element!

    @classmethod
    def from_list(cls, other_list=None): #Returns a new list from a given list
        lst = cls()
        if not other_list:
            return lst
        for value in reversed(other_list):
            lst.push(value)
        return lst

    @property
    def head(self):
        return self._head

    @property
    def size(self): #Returns length of list
        count = 0
        node = self._head
        while node is not None:
            count += 1
            node = node.next
        return count

    def is_empty(self): #Needs to return a boolean #Checks if this is an empty list
        return self.head is None 

    def peek(self): #Needs to view the head data without removing it
        if self.head is None:
            return None
        return self.head.datum
    
    def push(self, data): #Adds a new head
        new_obj = Element(data, self._head)
        self._head = new_obj

    def pop(self): #Return the value of the head. If there's a head, make the next element the new head. 
        value = self.peek()
        if self.head is not None:
            self._head = self._head.next
        return value
    
    def to_list(self): #Turns my List item into a plain Python list
        result = []
        node = self._head
        while node is not None:
            result.append(node.datum)
            node = node.next
        return result
    
    def reverse(self): #Creates a new list, but in reverse
        rev = SimpleLinkedList()
        node = self._head
        while node is not None:
            rev.push(node.datum)
            node = node.next
        return rev