import z3

# def encode_username(username):
#     encData = []
#     for i in username:
#         o = ord(i) % 0xA
#         o += 2
#         if o > 0xA:
#             o -= 0xA
#         encData.append(chr(o))

#     return ''.join(encData)


# def encode_serial(serial):
#     encData = []
#     for i in serial:
#         o = ord(i) % 10
#         encData.append(chr(o))
#     return ''.join(encData)


def encode_username(x,i):
    o = ord(x) % 0xA
    o ^= i
    o += 2
    if o > 0xA:
        o -= 0xA
    return o


def get_serial(userName):
    solver = z3.Solver()
    varNames = []
    for i in range(len(userName)):
        x = z3.BitVec('v%d' % i, 32)
        solver.add(x >= ord('A'))
        solver.add(x <= ord('z'))
        solver.add(encode_username(userName[i],i) == (x % 10))
        varNames.append(x)

    if solver.check() == z3.sat:
        model = solver.model()
        return ''.join([chr(model[i].as_long()) for i in varNames])
# encUserName = encode_username('1')
# print(encUserName)

# encSerial = encode_serial('2')
# print(encSerial)


serial = get_serial('123')
print(serial)
