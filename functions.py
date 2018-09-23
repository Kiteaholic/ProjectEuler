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
