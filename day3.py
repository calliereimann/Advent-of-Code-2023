import unittest

#Part 1 code

#My first idea is to scan the data into a 2d matrix, comparing coordinates for each number, but that would be absurdly computationally expensive. Not impossible by any means, but deeply painful. Maybe scanning as tuples? Line number, head, length, value? Where Value is either an int or a symbol. Maybe list of things considered 'valid' symbols. Dictionary of Dictionaries, maybe? Each row is a key for the first dictionary, then the column is the secondary key? numbers never wrap, so we can give them clear and precise row numbers, too

def scanline(line):
    output = {}
    loopmax = len(line)
    index = 0 
    while index < loopmax:
        if line[index] == ".":
            index+=1
            continue
        elif line[index].isdecimal():
            check = 1
            while line[index+check].isdecimal():
                check +=1
            output[index] = (check, int(line[index:index+check]))
            index += check
        else:
            output[index] = ('symbol', line[index])
            index +=1
    return output



#Part 2 code



class Tests(unittest.TestCase):
    def test_linescan(self):
        assert scanline("...23%..154..@...876...!@") == {3: (2, 23), 5:('symbol', '%'), 8:(3,154), 13:('symbol', '@'), 17:(3,876), 23:('symbol', '!'), 24:('symbol', '@')}
    
    
with open("day3.txt") as f:
   data = f.read()#

if __name__ == "__main__":
    pass