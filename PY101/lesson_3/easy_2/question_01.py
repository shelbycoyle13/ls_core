# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

reversed_list = numbers[::-1]

print(reversed_list)

reversed_list2 = list(reversed(numbers))

print(reversed_list2)