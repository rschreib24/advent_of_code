import math

inputs = []
with open("/Users/robert/Desktop/code/puzzle1/input.txt") as file:
    for line in file: 
        line = int(line.strip())
        inputs.append(line)

#iterInputs = iter(inputs)
for i, first in enumerate(inputs):
    iterInputs = inputs[i:]
    for second in iterInputs:
        if int(first) + int(second) == 2020:
           print('first: {} \nsecond: {}\nsum: {}\nmultiplied: {}'.format(first,second,first+second,first*second))
           break

