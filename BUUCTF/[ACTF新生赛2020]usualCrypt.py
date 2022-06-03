import base64

# 首先根据调用汇编代码揭密第第二层加密
# 再换表base64解密
string1 = "ABCDEFQRSTUVWXYPGHIJKLMNOZabcdefghijklmnopqrstuvwxyz0123456789+/="
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

print(str.maketrans(string1, string2))
print('ZmxhZ3tiGNXlXjHfaDTzN2FfK3LycRTpc2L9'.translate(str.maketrans(string1, string2)))
