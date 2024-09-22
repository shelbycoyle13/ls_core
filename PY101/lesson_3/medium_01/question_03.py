# Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# What is the key difference between these implementations?

print(add_to_rolling_buffer1([1, 2, 3], 3, 4))
print(add_to_rolling_buffer2([1, 2, 3], 3, 4))

# At a glance, it appears there is no difference because of the output. However, in the first function, the use of the append method mutates the original list.
# The second function initializes the buffer variable to buffer and adds the new element. Because of this syntax, a new list is created, therefore, no mutation like the first function. The buffer that is passed in as an argument is different than the buffer that is returned.
# Using print(id(buffer)) in the first line of the function body as well as in the last line will show that the first function uses mutation and the second function uses reassignment. The first function ids show the same memory address, while the second function ids show two different memory addresses.