# Build Profile
# Write a function build_profile that takes a first name and a last name, and any number of keyword arguments to add to a user's profile.

# print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}

def build_profile(first, last, **kwargs):
    start_dict = {'first_name': first, 'last_name': last}

    for key, value in kwargs.items():
        start_dict[key] = value
        
    return start_dict
    
print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}