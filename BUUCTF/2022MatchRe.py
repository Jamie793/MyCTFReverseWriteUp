
def unsignedRightShitf(data, offset):
    high = (data >> 56) & 0x7F
    binStr = bin(data)[2:]
    for i in range(offset):
        binStr = str(high) + binStr[:-1]
    
    return int(binStr,2)


print(unsignedRightShitf(0xF,5))


def encryptData(data: list) -> None:
    for i, v in enumerate(data):
        data[i] = ((v & 0x55) << 1) | (unsignedRightShitf(v & 0xAA, 1))
        data[i] = ((v & 0x33) << 2) | (unsignedRightShitf(v & 0xCC, 2))
        data[i] = ((v & 0x0F) << 4) | (unsignedRightShitf(v & 0xF0, 4))



data = [ord(i) for i in "qwertyuiopasdfghjklzxcvbnm7896456128"]
encryptData(data)
print(data)
print([hex(i) for i in data])
