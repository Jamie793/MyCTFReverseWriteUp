
import z3


def encode_pass(passwd):
    res = 0
    for i in passwd:
        ascii = ord(i) & 0xFF
        ascii -= 0x30
        res *= 0xA
        res += ascii
    res ^= 0x1234
    return hex(res)


def encode_username(username):
    res = 0
    for i in username.upper():
        ascii = ord(i) & 0xFF
        res += ascii
    res ^= 0x5678
    return res


def getPasswd(username: str):
    solver = z3.Solver()
    varNames = []
    res = None
    for i in range(len(username)):
        x = z3.BitVec('v%d' % i, 32)
        solver.add(x >= ord('0'))
        solver.add(x <= ord('z'))
        if res is None:
            res = x-0x30
        else:
            res = res * 0xA + (x-0x30)
        varNames.append(x)

    solver.add((res ^ 0x1234) == encode_username(username))

    if solver.check() == z3.sat:
        model = solver.model()
        return '"' + ''.join([chr(model[i].as_long()) for i in varNames]) + '"'
    else:
        return 'Not found...'


# encUserName = encode_username('ABC')
# encPasswd = encode_pass('abc')
# print(encUserName)
# print(encPasswd)

userName = 'aaaaaaaaaa'
passwd = getPasswd(userName)
print(passwd)
