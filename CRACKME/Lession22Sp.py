import z3

data = [0xD9, 0xFA, 0xE2, 0xF3, 0xE4, 0xF2, 0xAA, 0xE8, 0xF3, 0xAA,
        0xEE, 0xCA, 0xE8, 0xAA, 0xB8, 0xBA, 0xBA, 0xBE, 0x8A, 0xDD,
        0xEF, 0xE6, 0xE6, 0xAA, 0xCE, 0xE5, 0xE4, 0xEF, 0xAA, 0xAB,
        0xAA, 0xDD, 0xF8, 0xE3, 0xFE, 0xEF, 0xAA, 0xEB, 0xAA, 0xDE,
        0xFF, 0xFE, 0xE5, 0xF8, 0xE3, 0xEB, 0xE6, 0xAA, 0xAB]

key = data[0x12]
for i in data:
    print(chr(i ^ key), end='')


# data = 0x19372
# binData = bin(data)[2:]
# binData = binData[-1] + binData[0:-2]
# data = int(binData,2)
# data &= 0xFFFFFFFF
# print(chr(25820))

solver = z3.Solver()
tmp = 0
varNames = []

for i in range(255):
    x = z3.BitVec('v%d' % i, 32)
    solver.add(x > ord('A'))
    solver.add(x < ord('z'))
    tmp += x
    tmp <<= 1
    tmp &= 0xFFFFFFFF
    varNames.append(x)

solver.add(tmp == 0x19372)

if solver.check() == z3.sat:

        print('"'+''.join([chr(solver.model()[i].as_long()) for i in varNames])+'"')
