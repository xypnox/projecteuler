import math
import mlib

sums = 0

for num in range(3, 10**6):
    dgts = mlib.getDigits(num)
    fam = 0
    # print(num, dgts)
    for dgt in dgts:
        fam += math.factorial(dgt)
    if fam == num:
        print(fam)
        sums += fam

print("sum = ", sums)
