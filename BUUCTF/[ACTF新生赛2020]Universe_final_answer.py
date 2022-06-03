from operator  import itemgetter
import z3

v1 = z3.BitVec("v1", 32)
v2 = z3.BitVec("v0", 32)
v3 = z3.BitVec("v2", 32)
v4 = z3.BitVec("v3", 32)
v5 = z3.BitVec("v4", 32)
v6 = z3.BitVec("v6", 32)
v7 = z3.BitVec("v5", 32)
v8 = z3.BitVec("v7", 32)
v9 = z3.BitVec("v8", 32)

solver = z3.Solver()

solver.add(v2 > 0)
solver.add(v3 > 0)
solver.add(v4 > 0)
solver.add(v5 > 0)
solver.add(v6 > 0)
solver.add(v7 > 0)
solver.add(v8 > 0)
solver.add(v9 > 0)

solver.add(-85 * v9 + 58 * v8 + 97 * v6 + v7 + -45 * v5 +
           84 * v4 + 95 * v2 - 20 * v1 + 12 * v3 == 12613)

v11 = z3.BitVec("v9", 32)

solver.add(30 * v11 + -70 * v9 + -122 * v6 + -81 * v7 + -66 * v5 + -
           115 * v4 + -41 * v3 + -86 * v1 - 15 * v2 - 30 * v8 == -54400)
solver.add(-103 * v11 + 120 * v8 + 108 * v7 + 48 * v4 + -89 * v3 +
           78 * v1 - 41 * v2 + 31 * v5 - (v6 << 6) - 120 * v9 == -10283)
solver.add(71 * v6 + (v7 << 7) + 99 * v5 + -111 * v3 + 85 * v1 +
           79 * v2 - 30 * v4 - 119 * v8 + 48 * v9 - 16 * v11 == 22855)
solver.add(5 * v11 + 23 * v9 + 122 * v8 + -19 * v6 + 99 * v7 + -
           117 * v5 + -69 * v3 + 22 * v1 - 98 * v2 + 10 * v4 == -2944)
solver.add(-54 * v11 + -23 * v8 + -82 * v3 + -85 * v2 + 124 * v1 -
           11 * v4 - 8 * v5 - 60 * v7 + 95 * v6 + 100 * v9 == -2222)
solver.add(-83 * v11 + -111 * v7 + -57 * v2 + 41 * v1 + 73 * v3 -
           18 * v4 + 26 * v5 + 16 * v6 + 77 * v8 - 63 * v9 == -13258)
solver.add(81 * v11 + -48 * v9 + 66 * v8 + -104 * v6 + -121 * v7 +
           95 * v5 + 85 * v4 + 60 * v3 + -85 * v2 + 80 * v1 == -1559)
solver.add(101 * v11 + -85 * v9 + 7 * v6 + 117 * v7 + -83 * v5 + -
           101 * v4 + 90 * v3 + -28 * v1 + 18 * v2 - v8 == 6308)

solver.add(99 * v11 + -28 * v9 + 5 * v8 + 93 * v6 + -18 * v7 + -
           127 * v5 + 6 * v4 + -9 * v3 + -93 * v1 + 58 * v2 == -1697)


tmpDic = []
if solver.check() == z3.sat:
    print('Congratulation!')
    model = solver.model()
    for i in list(model):
        tmpDic.append(dict({'index': str(i), 'value': chr(model[i].as_long())}))


tmpDic.sort(key=lambda k: k['index'])
for i in tmpDic:
    print(i['value'],end='')
