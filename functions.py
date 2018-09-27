def factorise(n):
    l = []
    while n % 2 == 0:
        n = n // 2
        l.append(2)
    for i in range(3, n+1, 2):
        while n % i == 0:
            n = n // i
            l.append(i)
        if i > n:
            break
    return l


import math

def is_prime(n):
    if n == 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True                     




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



