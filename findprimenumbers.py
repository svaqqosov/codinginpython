import math


def isPrime(n):
    for i in range(3, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def countPrimes(n):
    if n <= 2:
        return 0
    count = 1
    for i in range(3, n, 2):
        if isPrime(i):
            count += 1
    return count


print(countPrimes(10))

print(countPrimes(499979))
