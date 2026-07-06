# print all the factors/divisors of a given number, as a list.
def factors():
    n = 5
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors

#better solution
def factorss():
    n = 18
    result = []
    for i in range(1,(n//2)+1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result

#optimal solution
from math import sqrt
def factorsss():
    n = 18
    result = []
    for i in range(1,int(sqrt(n))+1):
        if (n%i == 0):
            result.append(i)
            if(n//i != i):
                result.append(n//i)
    result.sort()
    return result

# making a frequency map / dictionary
nums = [3,3,3,3,4,6,9,5,7,9,5,8,99,6,8,85,4,7,9,42,4,5,3,34,8,7,0,7]
freq_map = {}
for i in range(0,len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]] = 1
x = 7
print(freq_map[x])


    
        
