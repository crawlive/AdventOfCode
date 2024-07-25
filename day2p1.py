import re;

#read_file = open("./input/day2Test.txt", 'r')
read_file = open("./input/day2Input.txt", 'r')

def detViability(game):
    colors = game.split(', ')
    for color in colors:
        if "red" in color:
            if int(re.search(r'\d+', color).group()) > 12:
                return False 
        if "blue" in color:
            if int(re.search(r'\d+', color).group()) > 14:
                return False 
        if "green" in color:
            if int(re.search(r'\d+', color).group()) > 13:
                return False 
    #print(colors)
    return True


total = 0

while read_file:
    line = read_file.readline()
    #print(line)
    if line == "":
        break
    gameNum = re.search('\d*(?=[\:])', line)
    games = re.findall('(?<=: )(.*)', line)
    gameMatches = games[0].split('; ')
    viable = True
    for matches in gameMatches:
        viable = detViability(matches)
        if(viable == False):
            break
    if viable == True:
        total += int(gameNum.group()) 
        print(gameNum[0])
print(total)
read_file.close()
