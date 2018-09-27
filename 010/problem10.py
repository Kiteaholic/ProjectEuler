# Summation of primes
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.


import math



def sieve_of_eratosthenes(n):
    primes = []
    if n < 2:
        return []
    sieve = [False] * (n)
    sieve[0] = True     # 0 ist keine Primzahl
    sieve[1] = True     # 1 ist keine Primzahl
    for i in range(int(math.sqrt(n)) + 1):
        if not sieve[i]:
            primes.append(i)
            j = (i * i)
            while j < n:
                sieve[j] = True
                j += i
    for i in range(int(math.sqrt(n)) + 1, n):
        if not sieve[i]:
            primes.append(i) 
    return primes

print(sum(sieve_of_eratosthenes(2000000)))
