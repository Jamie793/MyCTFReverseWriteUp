import hashlib
import base64
import z3

encData = [
    0x45, 0x6D, 0x42, 0x6D, 0x50, 0x35, 0x50, 0x6D, 0x6E, 0x37,
    0x51, 0x63, 0x50, 0x55, 0x34, 0x67, 0x4C, 0x59, 0x4B, 0x76,
    0x35, 0x51, 0x63, 0x4D, 0x6D, 0x42, 0x33, 0x50, 0x57, 0x48,
    0x63, 0x50, 0x35, 0x59, 0x6B, 0x50, 0x71, 0x33, 0x3D, 0x63,
    0x54, 0x36, 0x51, 0x63, 0x6B, 0x6B, 0x50, 0x63, 0x6B, 0x6F,
    0x52, 0x47
]


def decodeFlags():
    flags = []
    for i in range(len(encData)):
        for j in range(0x20, 0x7F):
            if j <= ord('@') or j > ord('Z'):
                if j <= ord('`') or j > ord('z'):
                    if j <= ord('/') or j > ord('9'):
                        if j == encData[i]:
                            flags.append(j)
                            break
                    else:
                        if (j - 48 + 3) % 10 + 48 == encData[i]:
                            flags.append(j)
                            break
                else:
                    if (j - 97 + 3) % 26 + 97 == encData[i]:
                        flags.append(j)
                        break
            else:
                if (j - 65 + 3) % 26 + 65 == encData[i]:
                    flags.append(j)
                    break
    flags = [chr(_) for _ in flags]
    return flags


flags = decodeFlags()
newFlags = ''
flag4 = flags[39:39+13]
flag3 = flags[26:26+13]
flag2 = flags[13:13+13]
flag1 = flags[0:13]


newFlags = flag2 + flag4 + flag1 + flag3

print(''.join(newFlags))


# print("flag{%s}" % ''.join(flags))


# solver = z3.Solver()
# varsName = []
# for i in range(len(encData)):
#     x = z3.BitVec("v%d" % i, 32)
#     z3.If(x <= ord('@') or x > ord('Z'),solver.add((x - 65 + 3) % 26 + 65 == encData[i]),1)
#     # solver.add(x > ord('@'))
#     # solver.add(x <= ord('Z'))
#     # solver.add(x <= ord('`'))
#     # solver.add(x > ord('z'))

#     # solver.add(x > ord('/'))
#     # solver.add(x <= ord('9'))

#     # solver.add((x - 48 + 3) % 10 + 48== encData[i])
#     # solver.add(x > 0x20)
#     # solver.add(x < 0x7F)
#     # z3.If(x <= ord('@') or x > ord('Z'),)
#     # if x <= ord('@') or x > ord('Z'):
#     #     if x <= ord('`@`') or x > ord('z'):
#     #         if x <= ord('/') or x > ord('9'):
#     #             solver.add(x == encData[i])
#     #         else:
#     #             solver.add((x - 48 + 3) % 10 + 48 == encData[i])
#     #     else:
#     #         solver.add((x - 97 + 3) % 26 + 97 == encData[i])
#     # else:
#     #     solver.add((x - 65 + 3) % 26 + 65 == encData[i])

#     varsName.append(x)


# if solver.check() == z3.sat:
#     print("Congratulations!")
#     model = solver.model()
#     for i in varsName:
#         print(hex(model[i].as_long()), ' ')
