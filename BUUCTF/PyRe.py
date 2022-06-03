import z3
print('Welcome to Re World!')
print('Your input1 is your flag~')
# l = len(input1)

# for i in range(l):
#     num = ((input1[i] + i) % 128 + 128) % 128
#     code += num

# for i in range(l - 1):
#     code[i] = code[i] ^ code[i + 1]


code = [
    '\x1f',
    '\x12',
    '\x1d',
    '(',
    '0',
    '4',
    '\x01',
    '\x06',
    '\x14',
    '4',
    ',',
    '\x1b',
    'U',
    '?',
    'o',
    '6',
    '*',
    ':',
    '\x01',
    'D',
    ';',
    '%',
    '\x13']

codeLen = len(code)
for i in range(codeLen):
    code[i] = ord(code[i])

for i in range(codeLen - 1):
    code[codeLen-2-i] ^= code[codeLen-1-i]


solver = z3.Solver()
varNames = []
for i, v in enumerate(code):
    x = z3.Int('v%d' % i)
    solver.add(x > 32)
    solver.add(x < 127)
    solver.add(((x + i) % 128 + 128) % 128 == v)
    varNames.append(x)
    

if solver.check() == z3.sat:
    model = solver.model()
    for i in varNames:
        print(chr(model[i].as_long()),end="")
