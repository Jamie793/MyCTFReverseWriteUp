from z3 import *
z = Solver()

text = "killshadow"
key = "adsfkndcls"

flag = []

for i, v in enumerate(text):
    x = z3.BitVec(i, 8)
    z.add(ord('A') <= x)
    z.add(ord('Z') >= x)
    z.add(ord('a') >= x)
    z.add(ord('z') >= x)
    z.add(((x - 0x27 - ord(key[i]) + 0x61) % 26 + 0x61) == ord(text[i]))
    flag.append(x)

if z.check() == z3.sat:
    tmp = z.model()
    for i in flag:
        print(tmp[i].as_long())
        print(chr(tmp[i].as_long()), end="")
