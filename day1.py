import re;
import os;
from pathlib import Path;

read_file = open("./input/advent.txt", 'r')
#read_file = open("./input/adventTest.txt", 'r')
code = 0

def giveNum(number): 
    if(number == "one"):
        return 1
    elif(number == "two"):
        return 2
    elif(number == "three"):
        return 3
    elif(number == "four"):
        return 4
    elif(number == "five"):
        return 5
    elif(number == "six"):
        return 6
    elif(number == "seven"):
        return 7
    elif(number == "eight"):
        return 8
    elif(number == "nine"):
        return 9

while read_file:
    
    line = read_file.readline()
    print(line)
    if line == "":
        break
    findWords = re.findall('(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    #print(findWords)
    firstNum = findWords[0]
    lastNum = findWords[-1]
    if(firstNum.isdigit() == False):
        #print(firstNum)
        firstNum = str(giveNum(firstNum))
    if(lastNum.isdigit() == False):
        #print(lastNum)
        lastNum = str(giveNum(lastNum))
    print(firstNum+lastNum)
    code += int(firstNum + lastNum)
    
    

print(code)
    
read_file.close()
