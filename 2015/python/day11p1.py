
ORDS = {
    chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)
}
ORDS['0'] = 0

CHARS = {
    v: k for k, v in ORDS.items()
}

ORD_A = ORDS['a']
ORD_Z = ORDS['z']

def add(left: str, right: str) -> str:
    if len(left) > len(right):
        rpad = right.zfill(len(left) - len(right) + 1)
        lpad = left
    else:
        lpad = left.zfill(len(right) - len(left) + 1)
        rpad = right
        
    newPassword = []

    carry = 0
    for i in range(1, len(lpad) + 1):
        x = -i
        l = lpad[x]
        r = rpad[x]
        v = ORDS[l] + ORDS[r] + carry
        if v > ORD_Z:
            carry = v - ORD_Z
            v -= 26
        else:
            carry = 0
        newPassword.append(CHARS[v])
    
    if carry > 0:
        newPassword.append(CHARS[carry])

    newPassword.reverse()
    return "".join(newPassword)

def increment(password):
    return add(password, "a")

def isValid(password):
    threeIncreasing = False
    duplicates = set()
    for i in range(len(password)):
        if password[i] in ['i', 'o', 'l']:
            return False
        if i < len(password) - 2:
            if password[i + 1] == chr(ord(password[i]) + 1) and password[i + 2] == chr(ord(password[i]) + 2):
                threeIncreasing = True
        if i < len(password) - 1:
            if password[i] == password[i + 1]:
                if 2*password[i] not in duplicates:
                    duplicates.add(2*password[i])

    return threeIncreasing and len(duplicates) > 1
    

# password = "vzbxkghb"
password = increment("vzbxxyzz")
while not isValid(password):
    password = increment(password)
print(password)

# print(increment("a"))
# assert increment("a") == "b"
# assert increment("z") == "aa"
# assert increment("yz") == "za"
# assert increment("zyz") == "zza"
