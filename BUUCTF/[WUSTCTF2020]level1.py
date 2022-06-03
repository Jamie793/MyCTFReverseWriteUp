
flag = [198, 232, 816, 200, 1536, 300, 6144, 984, 51200, 570,
        92160, 1200, 565248, 756, 1474560, 800, 6291456, 1782, 65536000]

for i in range(len(flag)):
    if (i+1) % 2 == 0:
        flag[i] //= (i+1)
    else:
        flag[i] >>= (i+1)

flag = [chr(_) for _ in flag]
print(''.join(flag))