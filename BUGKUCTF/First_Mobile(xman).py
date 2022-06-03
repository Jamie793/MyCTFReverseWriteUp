flag = [23, 22, 26, 26, 25, 25, 25, 26, 27, 28, 30, 30, 29, 30, 0x20, 0x20]

for i in range(len(flag)):
    for j in range(0x21, 0x7F):
        if ((j + flag[i]) % 61) * 2 - i == j:
            print(chr(j), end='')
