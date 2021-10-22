'''
Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other.
'''

from collections import Counter

def checkPermutation(s1, s2):

    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)