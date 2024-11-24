# A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?
    
# data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))
# print(unique_data == [4, 2, 1, 3]) # order not guaranteed

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
# unique_data = list(set(data))

unique_data = []
for num in data:
    if num not in unique_data:
        unique_data.append(num)

print(unique_data)
print(unique_data == [4, 2, 1, 3]) # order not guaranteed