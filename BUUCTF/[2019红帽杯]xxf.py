
hexStr = "C0 95 3A 7C 6B 40 BC CE"
hexStr = hexStr.split(" ")
hexStr.reverse()
for i in hexStr:
    print(chr(int(i,16)))