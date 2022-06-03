import binascii

key =[0x6E, 0x67, 0x6D, 0x62, 0x36, 0x88, 0x31, 0x33, 0x35, 0x33, 
  0x4D, 0x5C, 0x51, 0x55, 0x41, 0x40, 0x87]

# def encrypt(data):
#     newData = [0]* len(data)
#     for i, v in enumerate(data):
#         newData[i] = ord(v) + i + 1

#     return newData


for i, v in enumerate(key):
    key[i] = v ^ 9

for i in range(len(key)):
    for j in range(0x21,0x7F):
        if j + i + 1 == key[i]:
            print(chr(j),end='')

# print(''.join([chr(i) for i in encrypt("4576367537+")]))