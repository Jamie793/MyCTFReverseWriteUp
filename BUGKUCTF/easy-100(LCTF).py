

from Crypto.Cipher import AES


key = 'this_is_the_key.'
newKey = ''
for i in range(0, len(key), 2):
    newKey += key[i+1]
    newKey += key[i]


cipher = AES.new(newKey.encode(),AES.MODE_ECB)


byteArray = [21, -93, -68, -94, 86, 117, -19, -68, -92, 33,
            50, 118, 16, 13, 1, -15, -13, 3, 4, 103, -18,
            81, 30, 68, 54, -93, 44, -23, 93, 98, 5, 59]

str3 = ''
for i, v in enumerate(byteArray):
     byteArray[i] = (v + 256) % 256

print(cipher.decrypt(bytes(byteArray)).decode())
