# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

reverse_numbers1 = numbers[::-1]

print(reverse_numbers1)
print(reverse_numbers1 is numbers)

reverse_numbers2 = list(reversed(numbers))

print(reverse_numbers2)
print(reverse_numbers2 is numbers)