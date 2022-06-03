

def enc(charCode: int) -> str:
    tmp = 0
    if charCode <= ord('Z'):
        tmp = 90
    else:
        tmp = 122

    charCode = charCode + 13
    if tmp >= charCode:
        return charCode
    else:
        return charCode - 26


encData = 'PyvragFvqrYbtvafNerRnfl@syner-ba.pbz'
flags = []
for i in range(len(encData)):
    for j in range(ord('A'), ord('z')+1):

        if j > ord('Z') and j < ord('a'):
            continue

        if enc(j) == ord(encData[i]):
            flags.append(chr(j))
            break

print(len(encData), len(flags))
print("Flags:%s" % "".join(flags))
# 解密之后根据他给的flag格式带对应的地方把符号加上去得Flag
# flag{ClientSideLoginsAreEasy@flare-on.com}