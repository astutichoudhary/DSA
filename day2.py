# Checking if a given number is armstrong number or not.
n = 1634
num = n
sum = 0
nod = len(str(n))

while num > 0:
    last_digit = num % 10
    sum = sum + (last_digit ** nod)
    num //= 10

print(sum==n)