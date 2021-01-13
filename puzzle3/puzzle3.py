

inputs = []
with open("/Users/robert/Desktop/code/puzzle3/input.txt") as file:
    for line in file: 
        line = line.strip()
        inputs.append(line)

rowIncrement = 1
colIncrement = 3
colWidth = len(inputs[0])

treeCount = 0
col = 0

for row in list(range(0,len(inputs),rowIncrement)):
    col %= colWidth
    if inputs[row][col] == '#':
        treeCount += 1
    col += colIncrement

print(treeCount)
