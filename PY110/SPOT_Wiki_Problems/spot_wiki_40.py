# 40. Difference of Sum from Next Prime Number
# Given a List [] of n integers, find the minimum number to be inserted in the list, so that the sum of all elements of the list should equal the closest prime number.

#print(minimum_number([3,1,2]) == 1)
#print(minimum_number([5,2]) == 0)
#print(minimum_number([1,1,1]) == 0)
#print(minimum_number([2,12,8,4,6]) == 5) #sums to 32, adding 5 gets 37. Actually, we're trying to figure out the NEXT closest prime number. We go higher, not lower
#print(minimum_number([50,39,49,6,17,28]) == 2) #189, next prime number is 191, we go up again

"""
P
input = a list
output = an integer
explicit = we want the sum of all elements to equal a prime number, so we want to find out if there is a missing number that needs to be added to the list to equal the NEXT closest prime number
implicit = there may not even need to be anything added to a prime number

E

D
lists

A
sum the numbers in the list

if the sum is able to be divided by anything else other than itself, its NOT a prime number. so WHILE the sum is evenly divisible by something
    keep adding 1 to the sum

possible for range for divisor?

C
"""
def is_it_prime(num): #Best thing to do is create a helper function
    if num < 2: #Anything less than 2 is not a prime number
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1): #Check divisors up to the square root of the number, no need to check higher than that
            if num % i == 0: #If it's able to be evenly divisible
                return False #Then it's not a prime number
        return True #Otherwise, if we make it through the entire loop and haven't be able to be evenly divisible, then it is a prime number

def minimum_number(lst):
    total_sum = sum(lst)
    additional = 0

    while not is_it_prime(total_sum + additional): #While the current number is NOT prime
        additional += 1 #Keep adding until it is prime

    return additional

print(minimum_number([3,1,2]) == 1)
print(minimum_number([5,2]) == 0)
print(minimum_number([1,1,1]) == 0)
print(minimum_number([2,12,8,4,6]) == 5)
print(minimum_number([50,39,49,6,17,28]) == 2)