from pyexpat import model
import z3


def teaDecrypt(v: int, v2: int, key: list):
    delta = 0x458BCD42
    sum = delta * 64

    for _ in range(64):
        v2 -= ((v << 4) + key[2]) ^ (v + sum) ^ ((v >> 5) + key[3]) ^ 0x10
        v -= ((v2 << 4) + key[0]) ^ (v2 + sum) ^ ((v2 >> 5) + key[1]) ^ 0x20
        sum -= delta

    return [v, v2]


def splitData(data: list):
    datas = []
    tmp = []

    for i, v in enumerate(data):
        if i % 2 == 0:
            tmp.append(v)
            datas.append(tmp)
            tmp.clear()
        else:
            tmp.append(v)

    return datas


encData = [0]*6
for i, v in enumerate(encData):
    encData[i] = z3.Int('v%d' % i)

sovler = z3.Solver()
sovler.add(encData[0] == 0xDF48EF7E)
sovler.add(encData[1] == 0x20CAACF4)
sovler.add(encData[5] == 0x84F30420)

sovler.add(encData[2] - encData[3] == 0x84A236FF)
sovler.add(encData[3] + encData[4] == 0xFA6CB703)
sovler.add(encData[2] - encData[4] == 0x42D731A8)

if sovler.check() != z3.sat:
    exit(0)


print('Congratulations!')
dataModel = sovler.model()
print(dataModel)
datas = [dataModel[i].as_long() for i in encData]

for i in range(0, int(len(datas)/2), 2):
    print(teaDecrypt(datas[i], datas[i+1], [2, 2, 3, 4]))
