import math

inputs = []
with open("/Users/robert/Desktop/code/puzzle1/input.txt") as file:
    for line in file: 
        line = int(line.strip())
        inputs.append(line)

#iterInputs = iter(inputs)
for i, first in enumerate(inputs):
    iterInputs = inputs[i:]
    for j, second in enumerate(iterInputs):
        iteriterInputs = iterInputs[j:]
        for third in iteriterInputs:
            if first + second + third == 2020:
                print('first: {} \nsecond: {}\nthird: {} \nsum: {}\nmultiplied: {}'.format(first,second,third,first+second+third,first*second*third))
                break

