import unittest

#Part 1 code

#My first idea is to scan the data into a 2d matrix, comparing coordinates for each number, but that would be absurdly computationally expensive. Not impossible by any means, but deeply painful. Maybe scanning as tuples? Line number, head, length, value? Where Value is either an int or a symbol. Maybe list of things considered 'valid' symbols. Dictionary of Dictionaries, maybe? Each row is a key for the first dictionary, then the column is the secondary key? numbers never wrap, so we can give them clear and precise row numbers, too

def scanline(line):
    symbols = {}
    numbers = {}
    loopmax = len(line)
    print("loop length is " + str(loopmax))
    index = 0 
    while index < loopmax:
        if line[index] == ".":
            index+=1
            continue
        elif line[index].isdecimal():
            check = 1 #improved version of original idea, can handle arbitrarily long numbers and doesnt need lengthy if/else chains
            #technically overbuilt for what we need since the maximum digit length in the data is 3, but it's cleaner
            while index+check < loopmax and line[index+check].isdecimal():
                check +=1
            numbers[index] = (check, int(line[index:index+check]))
            index += check
        else:
            symbols[index] = line[index]
            index +=1
    output = (numbers, symbols)
    print(output)
    return output

#but the problem now is how to efficiently scan through the dictionaries for things nearby each other - well, i guess i don't actually care about efficiency as long as things are correct? but it just grates at me to have something that burns a ton of processing power

def dictify(data):
    output = []
    list = data.splitlines()
    index = 0
    while index < len(list):
        output.append(scanline(list[index])) 
        index +=1 
    return output #converting the original data into a list of tuples, one per row of the initial input - each tuple has a numbers chunk and a symbols chunk

def process(line, lastline, nextline = None):
    numbers, symbols = line
    score = 0
    for number in numbers: #in a dictionary, this scans over the keys, not the values, which is fortunate for us
        len, value = numbers[number]
        include = False
        if (number-1) in symbols or (number+len) in symbols:
            include = True
        if lastline != None and not include:
            discard, lastsymbols = lastline
            check = -1
            while check <= len and not include: #for efficiency, the moment include becomes true we stop looping and skip any remaining checks
                if (number+check) in lastsymbols:
                    print(str(value) + " passed lastsymbol check at " + str(number+check))
                    include = True
                else:
                    check +=1 
        if nextline != None and not include:
            discard, nextsymbols = nextline
            check = -1
            while check <= len and not include:
                if (number+check) in nextsymbols:
                    print(str(value) + " passed nextsymbol check at " + str(number+check))
                    include = True
                else:
                    check +=1 
        if include:
            print("including: " + str(value))
            score += value
    return score

def mainfunc(data):
    list = dictify(data)
    score = process(list[0], None, list[1])
    print(score)
    index = 1
    while index < (len(list)-1):
        val = process(list[index], list[index-1], list[index+1])
        score += val
        print(str(val) + ', ' + str(score))
        index +=1 
    score += process(list[-1], list[-2])
    return score    

#Part 2 code



class Tests(unittest.TestCase):
    def test_linescan(self):
        assert scanline("...23%..154..@...876...!@") == ({3:(2, 23), 8:(3,154), 17:(3,876)}, {5:'%', 13:'@', 23:'!', 24:'@'})
        
    def test_mainpart1(self):
        assert mainfunc("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""") == 4361 #oh im so frustrated by the way that multiline quotes interact with tabs - it makes perfect sense im just really frustrated
    
with open("day3.txt") as f:
   data = f.read()#

if __name__ == "__main__":
    print(mainfunc(data))