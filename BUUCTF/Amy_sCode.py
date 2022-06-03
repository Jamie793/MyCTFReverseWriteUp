v9 = [0] * 20
v9[0] = 149
v9[1] = 169
v9[2] = 137
v9[3] = 134
v9[4] = 212
v9[5] = 188
v9[6] = 177
v9[7] = 184
v9[8] = 177
v9[9] = 197
v9[10] = 192
v9[11] = 179
v9[12] = 153
v9[13] = 138
v9[14] = 145
v9[15] = 128
v9[16] = 137
v9[17] = 140
v9[18] = 175
v9[19] = 184


key = "LWHFUENGDJGEFHYDHIGJ"
for i,v in enumerate(v9):
    v9[i] = v - ord(key[i])

for i in range(0,len(v9)):
    v9[i] ^= i

print(''.join([chr(i) for i in v9]))