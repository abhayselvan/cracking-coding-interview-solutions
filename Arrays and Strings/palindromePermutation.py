'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­drome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
'''

from collections import Counter

def palindromePermutation(string):

    string = string.lower().replace(" ","")
    counter = Counter(string)

    oddCount = 0
    for letter in counter:
        if counter[letter] % 2 != 0:
            oddCount += 1

    return oddCount == 0 if len(string) % 2 == 0 else oddCount == 1


string = "Tact Coa"
print(palindromePermutation(string))