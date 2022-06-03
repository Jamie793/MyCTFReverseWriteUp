import z3
dword_40316D = 0
dword_403172 = 0


# def rol_data(data, count):
#     binData = bin(data)[2:].rjust(8,'0')
#     for i in range(count):
#         binData = binData[1:] + binData[0]
#     return (int(''.join(binData), 2))


def encode_passwdOri(password):
    global dword_40316D, dword_403172
    passwd = 0
    for i in password:
        o = ord(i) - 0x30
        passwd = passwd + passwd * 4
        passwd = o + passwd * 2

    passwd <<= 2
    dword_40316D = passwd

    passwd += 0x7479
    passwd ^= 0x313233
    passwd <<= 6
    passwd &= 0xFFFFFFFF
    dword_403172 = passwd

    return passwd


def encode_passwd(password):
    global dword_40316D, dword_403172
    passwd = 0
    for i in password:
        o = i - 0x30
        passwd = passwd + passwd * 4
        passwd = o + passwd * 2

    passwd <<= 2
    dword_40316D = passwd

    passwd += 0x7479
    passwd ^= 0x313233
    passwd <<= 6
    passwd &= 0xFFFFFFFF
    dword_403172 = passwd

    return passwd


def get_serial(data, len):
    assert len <= 0x14
    solver = z3.Solver()
    varNames = []
    tmp = None
    for i in range(len):
        x = z3.BitVec('v%d' % i, 32)
        solver.add(x >= ord('A'))
        solver.add(x <= ord('z'))
        if tmp is None:
            tmp = x - 0x30 
        else:
            tmp = (tmp + tmp * 4) * 2 + (x - 0x30)

        varNames.append(x)

    solver.add(data == (((((tmp << 2) + 0x7479) ^ 0x313233) << 6) & 0xFFFFFFFF))

    if solver.check() == z3.sat:
        print(123)

for i in range(1,0x14):
    print(get_serial(0x0F19DF23C, i))
# print(hex(encode_passwdOri('abc')).upper(), hex(
#     dword_40316D).upper(), hex(dword_403172).upper())
