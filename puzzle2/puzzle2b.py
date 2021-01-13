import re #regular expressions
from pprint import pprint


inputs = []
with open("/Users/robert/Desktop/code/puzzle2/input2.txt") as file:
    for line in file: 
        line = line.strip()
        parsedLine = re.split('-|: |\\s',line) #delimiters '-', ': ', any whitespace
 #       print(line, '\t', parsedLine)
        inputs.append(parsedLine)

validPasswordCount = 0
for line in inputs:
    firstposition, secondposition, letter, password = line

    isLetterAtfirstPosition = bool(password[int(firstposition)-1] == letter)
    isLetterAtsecondPosition = bool(password[int(secondposition)-1] == letter)

    if isLetterAtfirstPosition != isLetterAtsecondPosition: # XOR logic
        validPasswordCount += 1

print(validPasswordCount)
