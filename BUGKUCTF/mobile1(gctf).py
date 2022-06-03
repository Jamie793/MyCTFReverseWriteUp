flag = 'b9c77224ff234f27ac6badf83b855c76'
newFlags = ''
for i, v in enumerate(flag):
    if i & 0x1 == 0:
        newFlags += v

print(newFlags)