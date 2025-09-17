# Circular Buffer
# A circular buffer is a collection of objects stored in a buffer that is treated as though it is connected end-to-end in a circle. When an object is added to this circular buffer, it is added to the position that immediately follows the most recently added object, while removing an object always removes the object that has been in the buffer the longest.

# This works as long as there are empty spots in the buffer. If the buffer becomes full, adding a new object to the buffer requires getting rid of an existing object; with a circular buffer, the object that has been in the buffer the longest is discarded and replaced by the new object.

# Assuming we have a circular buffer with room for 3 objects, the circular buffer looks and acts like this:

# P1	P2	P3	Comments
# All positions are initially empty
# 1			Add 1 to the buffer
# 1	2		Add 2 to the buffer
# 2		Remove oldest item from the buffer (1)
# 2	3	Add 3 to the buffer
# 4	2	3	Add 4 to the buffer, buffer is now full
# 4		3	Remove oldest item from the buffer (2)
# 4	5	3	Add 5 to the buffer, buffer is full again
# 4	5	6	Add 6 to the buffer, replaces oldest element (3)
# 7	5	6	Add 7 to the buffer, replaces oldest element (4)
# 7		6	Remove oldest item from the buffer (5)
# 7			Remove oldest item from the buffer (6)
# Remove oldest item from the buffer (7)
# Remove non-existent item from the buffer (nil)

# Your task is to write a CircularBuffer class in Python that implements a circular buffer for arbitrary objects. The class should be initialized with the buffer size and provide the following methods:

# put: Add an object to the buffer
# get: Remove (and return) the oldest object in the buffer. Return None if the buffer is empty.
# You may assume that none of the values stored in the buffer are None (however, None may be used to designate empty spots in the buffer).

# buffer = CircularBuffer(3)

# print(buffer.get() is None)          # True

# buffer.put(1)
# buffer.put(2)
# print(buffer.get() == 1)             # True

# buffer.put(3)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True

# The above code should display True 15 times.

# My original answer was never going to solve any edge cases where putting other numbers in a non-ascending order would work, so I scrapped my answer. Let's focus on the LS answer as that focuses more on the insertion order and will work with edge cases.

class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size # Here we are just filling the buffer / list with None in all of the list positions for now
        self.next = 0 # This is the position where the next object will go
        self.oldest = 0 # This is the position where the oldest object is

    def put(self, obj):
        next_item = (self.next + 1) % len(self.buffer) #Starting off, (0 + 1) = 1. 1 / 3 = 0, remainder 1. next_item = 1, if self.next = 1, modulus = 2. if self.next = 2, modulus = 0 (in this case, this means that the next number position goes back to the beginning of the list)

        if self.buffer[self.next] is not None: # If the next number in our current list is not None (this also means the list is currently full):
            self.oldest = next_item #We updated the oldest pointer to point to the new oldest position

        self.buffer[self.next] = obj #The list element at the next position (index) will be replaced with the current object
        self.next = next_item #The next list position will be reassigned to the next item position

    def get(self):
        value = self.buffer[self.oldest] #value is the element of the list where the oldest element is
        self.buffer[self.oldest] = None #We want to remove the oldest element, so we replace it with None
        if value is not None: #If the element of the list happens to be None
            self.oldest += 1 #Add 1 to it and reassign to the new value
            self.oldest %= len(self.buffer) #Oldest element position modulo length of the list, and reassign it to this value

        return value #return the value of the oldest inserted element

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)

print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

# LS Bot points out:
# Notice the pattern: each time we add a new element to a full buffer, we (see the code in the put method):

# Calculate where the next position will be after this insertion
# Update oldest to point to that position (since we're about to overwrite the current oldest)
# Overwrite the current position with the new value
# Move the next pointer forward