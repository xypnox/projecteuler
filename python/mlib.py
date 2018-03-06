def getDigits(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x = x // 10
    return digits


def returnNumber(x):
    number = 0
    count = 0
    for dgts in x:
        number += dgts * 10**count
        count += 1
    return number


def get_prime_list(x):
    primes = []
    for k in range(2, x):
        a = True
        for i in primes:
            if k % i == 0:
                a = False
                break
            if i > int(k ** 0.5):
                break
        if a:
            primes.append(k)
    return primes


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


def circPerm(x):
    dgts = getDigits(x)
    perms = []

    while True:
        dgts.insert(0, dgts.pop())
        perms.append(returnNumber(dgts))
        if returnNumber(dgts) == x:
            break
    return perms


# print(circPerm(1234))
