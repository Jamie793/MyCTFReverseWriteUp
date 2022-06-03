import z3
key = 'Qsw3sj_lz4_Ujw@l'

sovler = z3.Solver()


varNames = []
for i in key:
    o = ord(i)
    if o > 64 and o <= 90:
        x = z3.Int('v%d' % o)
        sovler.add(x > 64)
        sovler.add(x <= 90)
        sovler.add(((x - 51) % 26 + 65) == o)
        varNames.append(x)
    elif o > 96 and o <= 122:
        x = z3.Int('v%d' % o)
        sovler.add(x > 96)
        sovler.add(x <= 122)
        sovler.add(((x - 79) % 26 + 97) == o)
        varNames.append(x)
    else:
        x = z3.Int('v%d' % o)
        sovler.add(x == o)
        varNames.append(x)

if sovler.check() == z3.sat:
    model = sovler.model()
    for i in varNames:
        print(chr(model[i].as_long()),end='')
