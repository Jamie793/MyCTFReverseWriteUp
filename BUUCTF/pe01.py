

import ctypes
import struct


encData = bytes([
    0x9C, 0xFF, 0xFF, 0xFF, 0x48, 0x00, 0x00, 0x00, 0x9E, 0xFF,
    0xFF, 0xFF, 0x99, 0xFF, 0xFF, 0xFF, 0x4E, 0x00, 0x00, 0x00,
    0x8A, 0xFF, 0xFF, 0xFF, 0x3D, 0x00, 0x00, 0x00, 0xA5, 0xFF,
    0xFF, 0xFF, 0x53, 0x00, 0x00, 0x00, 0xB6, 0xFF, 0xFF, 0xFF,
    0x80, 0xFF, 0xFF, 0xFF, 0x06, 0x00, 0x00, 0x00, 0x27, 0x00,
    0x00, 0x00, 0xA3, 0xFF, 0xFF, 0xFF, 0x75, 0x00, 0x00, 0x00,
    0x99, 0xFF, 0xFF, 0xFF, 0xBF, 0xFF, 0xFF, 0xFF
])


def encrypt(data, i):
    data = (16 * (data & 0xF)) | (data >> 4) & 0xF
    data = -data
    data ^= i + 0x41
    return data


for i in range(0, 17):
    for j in range(0x21, 0x7E):
        encD = encrypt(j, i)
        if encD == struct.unpack_from('<l', encData, i*4)[0]:
            print(chr(j),end='')


# index = 0
# for i in range(0, 17):
#     for j in range(0x21, 0x7E):
#         encD = encrypt(j, i)
#         if encD & 0xFF == encData[index] \
#                 and (encD >> 8) & 0xFF == encData[index+1]\
#                 and (encD >> 16) & 0xFF == encData[index+2]\
#                 and (encD >> 32) & 0xFF == encData[index+3]:
#             print(chr(j), i)
#     index += 4

    # if encD & 0xFF == encData[i] \
    # and (encD >> 8) & 0xFF == encData[i+1] \
    # and (encD >> 16) & 0xFF == encData[i+2] \
    # and (encD >> 32) & 0xFF == encData[i+3]:
    #     print(chr(j))

    # solver = z3.Solver()
    # varNames = []
    # for i in range(17):
    #     x = z3.BitVec("v%d" % i, 32)
    #     # solver.add(x > 0x20)
    #     # solver.add(x < 0x7F)
    #     solver.add(encrypt(i) ^ (i+0x41) == encData[i])

    # if solver.check() == z3.sat:
    #     print("Congratulation!!!")
    #     model = solver.model()
    #     for i in varNames:
    #         print(model[i].as_long())
