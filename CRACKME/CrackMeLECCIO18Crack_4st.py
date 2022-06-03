def rol(data, offset):
    binData = bin(data)[2:]
    binDataLen = len(binData)
    if binDataLen != 32:
        for _ in range(32-binDataLen):
            binData = '0'+binData

    for _ in range(offset):
        binData = binData[1:]+binData[0]

    return int(binData, 2) & 0xFFFFFFFF


def calc_license(userName):
    ebx = 0
    eax = 0

    # for i in range(len(userName)):
    #     eax = ord(userName[i])
    #     eax ^= i
    #     ebx += eax

    ecx = 0
    while True:
        eax = ord(userName[ecx])
        ecx += 1
        eax ^= ecx
        ebx += eax

        if ecx >= len(userName):
            break

    eax = rol(eax,0xC)
    eax += ebx
    return eax

print(calc_license('JamieVeryCool'))
