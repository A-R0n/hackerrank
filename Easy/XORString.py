# Exclusive or function returns true when
# inputs differ, one is true the other false
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'
    return res