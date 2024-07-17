import unittest 

#we're going card by card, so we just care about things that work on each individual line. the card number doesn't *currently* matter, but it probably will in the future. 
#every single card has the exact same formatting, which we can use for efficiency
#the card id, the winning numbers, and the active numbers, are all fixed-length
#so we can use substring tricks to make things a lot easier
#at the cost of having 'magic numbers', but what can ya do

def linesplit(line):
    cardid = line[0:9]
    winlist = line[9:40].strip().split(" ")
    mylist = line[42:]
    print (cardid,winlist,mylist)

linesplit("Card   5: 46 50 28 25 44 73  3 14 17 20 | 33 14 44 71 73 59 19 80 40 20  5  6 72 85 47 62 30 50 83 51 24 28  3 77 39")

class Tests(unittest.TestCase):
    def firsttest(self):
        pass

with open("day4.txt") as f:
   data = f.read()#

if __name__ == "__main__":
    pass