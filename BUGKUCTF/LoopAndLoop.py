import sys

def chec(data1, data2):
    if data2 - 1 <= 0:
        return data1
    r = 2 * data2 % 3
    if r == 0:
        return check1(data1, data2-1)
    elif r == 1:
        return check2(data1, data2-1)
    else:
        return check3(data1, data2-1)


def check3(arg1, arg2):
    for i in range(1, 10000):
        arg1 -= i

    return chec(arg1, arg2)


def check2(arg5, arg6):
    t = arg5
    if arg6 % 2 == 0:
        for i in range(1, 1000):
            t -= i

        return chec(t, arg6)
    else:
        for i in range(1,1000):
            t += i
        return chec(t, arg6)


def check1(data1, data2):
    for i in range(1, 100):
        data1 -= i
    return chec(data1, data2)

print(chec(0x6D6F1462,99))
# for i in range(99999999):
#     if chec(i,99) == 0x6D6F1462:
#         print(i)

