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
        r = math.floor(math.sqrt(n)
        f = 5
        while f <= r
            if n % f == 0:
                return False
                    




def sieve_of_eratosthenes(n):
    sieve = [True for _ in range(n - 1) ]
    sieve[0] = [False]
    for item in enumeratesieve:



    
    return sieve    




print(sieve_of_eratosthenes(10))
