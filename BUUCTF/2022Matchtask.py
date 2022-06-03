# from secret import flag

# key = "xxxx" # not real key

# cipher = ""
# for i, c in enumerate(flag):
#     cipher += chr(ord(c) ^ ord(key[i%4]))

# with open("cipher", "w") as f:
#     f.write(cipher)



import z3

keys = []
flags = []

for 