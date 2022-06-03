from z3 import *

c = [
        144,
        163,
        158,
        177,
        121,
        39,
        58,
        58,
        91,
        111,
        25,
        158,
        72,
        53,
        152,
        78,
        171,
        12,
        53,
        105,
        45,
        12,
        12,
        53,
        12,
        171,
        111,
        91,
        53,
        152,
        105,
        45,
        152,
        144,
        39,
        171,
        45,
        91,
        78,
        45,
        158,
        8]

b = 179
solver = Solver()

varNames = []
for i in range(len(c)):
        x = z3.BitVec("v%d" % i, 32)
        solver.add(x > 0x20)
        solver.add(x <= 0x7E)
        solver.append(x * 33 % b == c[i])
        varNames.append(x)


if solver.check() == z3.sat:
        print("======")
        tmp = solver.model()
        for i in varNames:
                # print(tmp[i].as_long())
                print(chr(tmp[i].as_long()), end="")