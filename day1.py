# Extracting the digits of a number given.
n = 56345
num = n
while num>0:
    last_digit = num%10
    print(last_digit)
    num //= 10 
    # //= refers to float division which returns an integer value after dividing. example 543//10 = 54 instead of 54.3
    # the number is rounded off to lower integer value.


# Counting the digits of a give number.
n = 43325612300
count = 0
num = n
while num>0:
    count += 1
    num //= 10
print(count)
# we initialise a variable count with 0, add 1 for every iteration of the loop, 
# which also performs float division with 10 to the number thus
# finally it leads to 0, like 4345,434,34,4,0.
# the loop terminates just before reaching zero.


# Checking if a given number is a palindrome or not.
n = 12333221
result = 0
num = n
while num>0:
    last_digit = num%10
    result = (result * 10) + last_digit
    num //= 10
print(n==result)
# we introduce a variable result, where we will store our reversed number.
# we extract the last digit first, by dividing with 10, the remainder is the last digit
# the remainder is added to the result multiplied by 10, in every iteration, thus building the inputted number, backwards
# lastly we check if result and inputed numbers are equal or not and return a boolean value respectively.