import base64
encData = [0x65, 0x33, 0x6E, 0x69, 0x66, 0x49, 0x48, 0x39, 0x62, 0x5F,
           0x43, 0x40, 0x6E, 0x40, 0x64, 0x48]

flags = ""
for i, v in enumerate(encData):
    flags += chr(v - i)

print(base64.b64decode(flags))
