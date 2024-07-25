import re;
import os;
from pathlib import Path;

#read_file = open("./input/day3Test.txt", 'r')
read_file = open("./input/day3Input.txt", 'r')

def findSurroundingCoordinates(coordinate):
    for x in range(coordinate[0] - 1, coordinate[0] + 2):
        for y in range(coordinate[1] - 1, coordinate[1] + 2):
            if((x,y) != coordinate):
                adjacentCoordinates.append((x,y))
        
        
adjacentCoordinates = []  
numberCoordinates = []
xCoordinate = 0
numbers = []
while read_file:
    line = read_file.readline()
    for num in re.finditer(r"\d+", line):
        numbers.append((int(num.group(0)), [xCoordinate, num.start(), num.end()]))
    yCoordinate = 0
    for character in line.strip():                          #enumerate?
        if not character.isalnum() and character != '.':
            position = (xCoordinate, yCoordinate)
            findSurroundingCoordinates(position)
        if character.isnumeric():
            position = (xCoordinate, yCoordinate)
            numberCoordinates.append(position)
        yCoordinate += 1
    if line == "":
        break
   
    xCoordinate += 1
    
overlapCoordinates = sorted(set(adjacentCoordinates) & set(numberCoordinates))

total = 0
for part in overlapCoordinates:
    for num in numbers:
        if part[0] == num[1][0] and part[1] in range(num[1][1], num[1][2]):
            total += num[0]
            numbers.remove(num)
            
print(total)

read_file.close()

