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


def sieve_of_eratosthenes(n):
    sieve = [True for _ in range(n - 1) ]
    sieve[0] = [False]
    for item in enumeratesieve:



    
    return sieve    




print(sieve_of_eratosthenes(10))
