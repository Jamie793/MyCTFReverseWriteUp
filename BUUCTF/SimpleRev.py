from operator import le
import string


text = 'killshadow'

key = "ADSFKNDCLS"

key = str.lower(key)
dic = string.ascii_uppercase+string.ascii_lowercase

result = []
for i in range(len(text)):
    for j in dic:
        if (ord(j) - 39 - ord(key[i]) + 97) % 26 + 97 == ord(text[i]):
            result.append(j)
            break
    
print(str.lower(''.join(result)))