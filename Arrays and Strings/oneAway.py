'''
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away.
'''

def compareStrings(s1, s2, isSameLength):

    i = j = 0
    skip = True

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if skip:
                skip = False
                i += 1
                j += isSameLength
            else:
                return False
        else:
            i += 1
            j += 1

    return True    

def oneAway(s1, s2):

    lengthDiff = len(s1) - len(s2)

    if abs(lengthDiff) > 1:
        return False

    if lengthDiff > 0:
        return compareStrings(s1, s2, False)
    if lengthDiff < 0:
        return compareStrings(s2, s1, False)
    return compareStrings(s1, s2, True)

strings = [["pale","ple"],["pales","pale"],["pale","bale"],["pale","bake"]]
for s1, s2 in strings:
    print(oneAway(s1,s2))

    
    