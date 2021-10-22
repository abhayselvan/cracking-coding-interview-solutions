'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

# ask if ascii or unicode string because ascii has only 128 strings so if length of given string is greater than 128, we can return false.

def isUnique(string): #without using additional data structure

    # Time Complexity: O(nlogn)
    # Space Complexity: O(1)

    string.sort()

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            return False
    return True

def isUnique(string): #using additional space
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    numSet = set()

    for ch in string:
        if ch in numSet:
            return False
        numSet.add(ch)
    return True
