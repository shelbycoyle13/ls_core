# What will the following code output? Try to answer without running the code.

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5] #This variable points to a list with two dicts and 3 integers in it
my_list2 = my_list1.copy() #This variable points to a shallow copy of my_list1, meaning that only the outer element of the list gets copied, not the inner elements such as the dicts. The inner elements are shared and have pointers.
my_list2[0]['first'] = 42 #We take the first element (the dict) and set the key equal to a value of 42
print(my_list1) #This first list will be affected by any mutations, this should print the entire list objectm including the change of setting the key value to 42
