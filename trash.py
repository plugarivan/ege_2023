def rot13(message):
    res = ''
    for item in message:
        if (ord(item)>= ord('A') and ord(item)<= ord('M')) or (ord(item)>= ord('a') and ord(item)<= ord('m')):
            res += chr(ord(item)+13)
        elif (ord(item)>= ord('N') and ord(item)<= ord('Z')) or (ord(item)>= ord('n') and ord(item)<= ord('z')):
            res += chr(ord(item)-13)
        else:
            res += item
    return res





