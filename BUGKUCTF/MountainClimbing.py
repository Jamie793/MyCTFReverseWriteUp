import random
random.seed(0x0C)


def generateKey():
    for i in range(20):
        for j in range(i):
            print(hex(random.randint(0, 999)))


def encrypt(data):
    for i, v in enumerate(data):
        tmp = i & 0x80000001
        if  tmp < 0:
            tmp -= 1
            tmp ^= 0x0FFFFFFFE
            tmp += 1

        if tmp != 0:
            data[i] ^= 4

    print([chr(i) for i in data])


# data = '2344320243024003242'
# encrypt([ord(i) for i in data])
generateKey()