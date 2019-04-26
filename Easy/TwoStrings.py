## Given two strings, determine if they have
## a smaller substring.
## Return 'YES' if substring is shared.
## Return 'NO' if no substring exists.
def twoStrings(s1, s2):
    return 'YES' if any(i in s2 for i in s1 ) else 'NO'
## only returns false if all values are false