# Extracting the digits of a number given.
n = 56345

num = n
while num>0:
    last_digit = num%10
    print(last_digit)
    num //= 10 
    # //= refers to float division which returns an integer value after dividing. example 543//10 = 54 instead of 54.3
    # the number is rounded off to lower integer value.
