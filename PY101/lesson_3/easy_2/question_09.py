# We have most of the Munster family in our ages dictionary:

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

# Add entries for Marilyn and Spot to the dictionary:

additional_ages = {'Marilyn': 22, 'Spot': 237}

# ages['Marilyn'] = 22
# ages['Spot'] = 237

# print(ages)

# I don't remember this method, but this is very handy!

ages.update(additional_ages)

print(ages)