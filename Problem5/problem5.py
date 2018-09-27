# Smallest multiple
# Problem 5 
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def factorise(n):
    l = []
    while n % 2 == 0:
        n = n // 2
        l.append(2)
    for i in range(3, n + 1, 2):
        while n % i == 0:
            n = n // i
            l.append(i)
        if i > n:
            break
    return l

factors = []
for i in range(2,20):
   factors.append(factorise(i))
# for fact in factors:


print(factors)

