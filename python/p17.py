import mlib

tens = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    0: ''
}
teens = {
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
    0: ''
}
digits = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: ''
}

sum_of_length = 0


def getLength(n):
    pos = 0
    dgts = mlib.getDigits(n)
    length = 0
    print(n)
    for dgt in mlib.getDigits(n):
        if pos == 0:
            if len(dgts) >= 2 and dgts[1] == 1:
                length += len(teens[dgt])
                # print(teens[dgt])
            else:
                length += len(digits[dgt])
                # print(digits[dgt])
            pos += 1
        elif pos == 1:
            if dgt == 1 and dgts[0] != 0:
                pass
            else:
                length += len(tens[dgt])
                # print(tens[dgt])
            pos += 1
        elif pos == 2:
            length += len(digits[dgt])
            # print(digits[dgt])
            if dgt != 0:
                length += len('hundred')
                # print('hundred')
                if dgts[0] == 0 and dgts[1] == 0:
                    pass
                else:
                    length += len('and')
                    # print('and')
            pos += 1
        elif pos == 3:
            length += len(digits[dgt])
            # print(digits[dgt])
            if dgt != 0:
                length += len('thousand')
                # print('thousand')
            pos += 1
        else:
            pass
    return length


for n in range(1, 1001):
    sum_of_length += getLength(n)

print(sum_of_length)
