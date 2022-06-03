
flags = [0]*33

flags[0] = 119
flags[1] = 99
flags[4] = 50
flags[17] = 114
flags[29] = 102
flags[17] = 114
flags[24] = 95
flags[2] = 116
flags[9] = 99
flags[32] = 125
flags[19] = 118
flags[5] = 48
flags[14] = 110
flags[15] = 100
flags[8] = 123
flags[18] = 51
flags[28] = 95
flags[21] = 114
flags[6] = 50
flags[22] = 115
flags[31] = 110
flags[12] = 95
flags[7] = 48
flags[16] = 95
flags[11] = 112
flags[23] = 101
flags[30] = 117
flags[10] = 112
flags[13] = 64
flags[3] = 102
flags[26] = 114
flags[20] = 101
flags[25] = 64
flags[27] = 101

for i in range(len(flags)):
    print(i, chr(flags[i]))

print(''.join([chr(i) for i in flags]))
