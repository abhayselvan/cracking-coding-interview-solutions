'''
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, your method should return the original string. 
You can assume the string has only uppercase and lowercase letters (a - z).
'''

def stringCompression(string):

    if len(string) < 3:
        return string

    start = 0
    count = 1
    result = []

    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            result.append(string[start])
            result.append(str(count))
            start = i
            count = 1
        else:
            count += 1

    result.append(string[start])
    result.append(str(count))

    return "".join(result) if len(result) < len(string) else string

string = "aabcccccaaa"
print(stringCompression(string))