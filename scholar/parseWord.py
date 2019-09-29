import textract
import re
import sys

def parseDoc(filename):
    text = textract.process(filename)
    content = text.decode("utf-8") 
    return content

def getRef(words, j):
    res = words[j]
    j -= 1
    while j >= 0:
        firstChar = words[j][0]
        if firstChar.isupper() or \
            firstChar == '&' or \
            (firstChar == '(' and '20' not in words[j] and '19' not in words[j]) or \
            'al' in words[j] or \
            'and' in words[j] or \
            'et' in words[j]:
            res = words[j] + ' ' + res;
            j -= 1
        else:
            break

    # clean
    while not res[-1].isdigit():
        res = res[:-1]
    res = res.replace('(', '')
    res = res.replace('&', ',')
    return res

def extract_ref(content):
    words = content.split()
    refList = []
    for i in range(len(words)):
        word = words[i]
        if '20' in word or '19' in word:
            ref = getRef(words, i)
            refList.append(ref)
    return refList

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please give a file name")
        exit()

    filename = sys.argv[1]
    content = parseDoc(filename)

    refList = extract_ref(content)

    for line in refList:
        print(line)

    



