import unittest 

#we're going card by card, so we just care about things that work on each individual line. the card number doesn't *currently* matter, but it probably will in the future. 
#every single card has the exact same formatting, which we can use for efficiency
#the card id, the winning numbers, and the active numbers, are all fixed-length
#so we can use substring tricks to make things a lot easier
#at the cost of having 'magic numbers', but what can ya do

def doublezerofilter(line):
    index = line.find("  ") #semi efficiently strips out double zeroes so that the split method in linesplit doesnt create '' values 
    while index != -1:
        line = line[:index] + line[index+1:]
        index = line.find("  ")
    return line

def linesplit(line):
    cardid = line[0:9]
    winlist = doublezerofilter(line[9:40].strip()).split(" ")
    mylist = doublezerofilter(line[42:].strip()).split(" ")
    return (cardid,winlist,mylist)

def cardcheck(winlist, mylist):
    score = 0
    for item in mylist:
        if item in winlist:
            if score ==0:
                score = 1
            else:
                score *= 2
    return score

def part1body(data):
    list = data.splitlines()
    score = 0
    for item in list:
        (discard, winlist, mylist) = linesplit(item)
        score += cardcheck(winlist, mylist)
    return score

#we're in part 2 now, and the card numbers matter a lot, so its a good thing we're saving them 

class Tests(unittest.TestCase):
    def test_cardcheck(self):
        assert cardcheck((41,48,83,86,17), (83,86,  6, 31, 17,  9, 48, 53)) == 8
        assert cardcheck((13, 32, 20, 16, 61),(61, 30, 68, 82, 17, 32, 24, 19)) == 2
        assert cardcheck((1, 21, 53, 59, 44),(69, 82, 63, 72, 16, 21, 14,  1)) == 2
        assert cardcheck((41, 92, 73, 84, 69),(59, 84, 76, 51, 58,  5, 54, 83)) == 1
        assert cardcheck((87, 83, 26, 28, 32),(88, 30, 70, 12, 93, 22, 82, 36)) == 0


with open("day4.txt") as f:
   data = f.read()#

if __name__ == "__main__":
    print(part1body(data))