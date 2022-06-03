BASE64_ENCODE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                 'w', 'x', 'y', 'z', '0', '1', '2', '3',
                 '4', '5', '6', '7', '8', '9', '+', '/']


def base64Encode(data: str):
    data = [ord(i) for i in data]
    for i in data:
        if i > 128 or i < 0:
            return None
        
    
    
    tmp = [0] * 4
    for i in data:



base64Encode('ABC')

