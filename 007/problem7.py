#10001st prime
#Problem 7 
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?

def is_prime(list, num):
    for prime in list:
        if num % prime == 0:
            return False
    return True


primes = []
count = 2
while len(primes) < 10001:
    if is_prime(primes, count):
        primes.append(count)
    count += 1

print(primes)
print(primes[-1])
