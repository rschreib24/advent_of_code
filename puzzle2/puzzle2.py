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
    minOccurance, maxOccurance, letter, password = line
    numOccurances = password.count(letter)
    if int(minOccurance) <= numOccurances and numOccurances <= int(maxOccurance):
        validPasswordCount += 1

print(validPasswordCount)
