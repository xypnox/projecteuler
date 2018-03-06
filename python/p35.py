import mlib

primes = mlib.get_prime_list(1000000)

noOfC = 0

for prime in primes:
    cond = True
    for n in mlib.circPerm(prime):
        if n not in primes:
            cond = False
    if cond is True:
        print(prime)
        noOfC += 1


print("No Of Circular primes less than a million are : ", noOfC)
