# our prime list is empty here
primes = []


def is_prime(x):
    a = True
    for i in primes:
        if x % i == 0:
            a = False
            break
        if i > int(x ** 0.5):
            break
    if a:
        primes.append(x)
    return a


# this loop simply runs the fxn to add newer primes
for i in range(2, 9999):
    is_prime(i)

primes2 = []

for prime in primes:
    if prime > 1000:
        primes2.append(prime)


def getDigits(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x = x // 10
    return digits


def permutate(x):
    digits = getDigits(x)
    perms = []
    for d1 in digits:
        for d2 in digits:
            if d2 != d1:
                for d3 in digits:
                    if d3 not in [d1, d2]:
                        for d4 in digits:
                            if d4 not in [d1, d2, d3]:
                                n = d1*1000 + d2*100 + d3*10 + d4
                                perms.append(n)
    return perms


def areEqualspaced(n1, n2, n3):
    if n1 - n2 == n2 - n3 or n2 - n3 == n3 - n1 or n3 - n1 == n1 - n2:
        return True
    else:
        return False


for prime in primes2:
    permPrimes = []
    for perm in permutate(prime):
        if perm in primes2:
            permPrimes.append(perm)
    if len(permPrimes) >= 3:
        for perm in permPrimes:
            for perm2 in permPrimes:
                if perm2 != perm:
                    for perm3 in permPrimes:
                        if areEqualspaced(perm, perm2, perm3):
                            print(perm, perm2, perm3)

print("Digits of 1234 are : ", getDigits(1234))
print("Permutations of 1234 are : ", permutate(1234))
