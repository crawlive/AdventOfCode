import re;
import os;
from pathlib import Path;

#read_file = open("./input/day4Test.txt", 'r')
read_file = open("./input/day4Input.txt", 'r')

def prodVal(num):
    x = 1
    for i in range(1, num):
        x*=2
    return x

total = 0
while read_file:
    line = read_file.readline()
    if line == "":
        break
    winningNums = (list(map(int, re.search('(?<=\:).*(?=\|)', line).group(0).strip().split())))
    scratchedNums = (list(map(int, re.search('(?<=\|).*', line).group(0).strip().split())))
    matchSet = set(winningNums) & set(scratchedNums)
    total += (len(matchSet)) if len(matchSet) <= 2 else prodVal(len(matchSet))
 
print(total)