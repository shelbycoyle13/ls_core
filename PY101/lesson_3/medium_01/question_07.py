# One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42                  # This will mutate the original dict
        value["gender"] = "other"           # This reassigns, so the keys point to a new string; this reassignment mutates the dictionary as a whole

# After writing this function, he typed the following code:

mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key with his tail. Did the family's data get ransacked? Why or why not?

# Initially, I thought because there was no final return statement at the end of the loop, that this might not work and the data wouldn't be changed. 
# However, the correct answer is that when dictionaries are passed to the function, the reference to the dictionary is passed, not a copy. Changes made within the function directly affect the dictionary. If we wanted to have a separate dictionary with the different values, we would need to reassign demo_dict. In this case, the function uses it as is, so the object that gets changed is indeed the munsters object.
# Here is something we would use for a deep copy (because this is a nested dictionary):

# import copy
# demo_dict_copy = copy.deepcopy(demo_dict)