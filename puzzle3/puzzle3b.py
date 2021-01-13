
def getNumberOfTrees(colI,rowI):
    inputs = []
    with open("/Users/robert/Desktop/code/puzzle3/input.txt") as file:
        for line in file: 
            line = line.strip()
            inputs.append(line)

    file.close()

    rowIncrement = rowI
    colIncrement = colI
    colWidth = len(inputs[0])

    treeCount = 0
    col = 0

    for row in list(range(0,len(inputs),rowIncrement)):
        col %= colWidth
        if inputs[row][col] == '#':
            treeCount += 1
        col += colIncrement

    return treeCount

slope1 = getNumberOfTrees(1,1)
slope2 = getNumberOfTrees(3,1)
slope3 = getNumberOfTrees(5,1)
slope4 = getNumberOfTrees(7,1)
slope5 = getNumberOfTrees(1,2)

print(slope1 * slope2 * slope3 * slope4 * slope5)



