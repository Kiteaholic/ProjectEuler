# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def factorise(n):
    l = []
    while n % 2 == 0:
        n = n // 2
        l.append(2)
    for i in range(3, n // 2, 2):
        while n % i == 0:
            n = n // i
            l.append(i)
        if i > n:
            break
    return l

print(max(factorise(600851475143)))
