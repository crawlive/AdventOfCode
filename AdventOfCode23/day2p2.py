import re;

#read_file = open("./input/day2Test.txt", 'r')
read_file = open("./input/day2Input.txt", 'r')

def detPower(game):
    print(game)
    redMax, blueMax, greenMax = 0, 0, 0
    for color in game:
        #print(color)
        if "r" in color:
            redVal = int(re.search(r'\d+', color).group())
            if redVal > redMax:
                redMax = redVal
        if "b" in color:
            blueVal = int(re.search(r'\d+', color).group())
            if blueVal > blueMax:
                blueMax = blueVal
        if "g" in color:
            greenVal = int(re.search(r'\d+', color).group())
            if greenVal > greenMax:
                greenMax = greenVal 

    power = redMax * greenMax * blueMax
    #print(power) 
    return power

    
totalPower = 0
while read_file:
    line = read_file.readline()
    #print(line)
    if line == "":
        break
    gameNum = re.search('\d*(?=[\:])', line)
    gameColors = re.findall('(\d+ [{b|r|g}])', line)
    totalPower += detPower(gameColors)
        
print(totalPower)
read_file.close()
