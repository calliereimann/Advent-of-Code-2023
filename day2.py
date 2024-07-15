import unittest

colorlimits = {'red': 12, 'green':13, 'blue':14} #number of balls of each color

def interpretevent(eventstring):
    #takes event, returns true if all values are within the limits
    list = eventstring.split(",")
    eventValid=True
    for item in list:
        item = item.strip()
        if item == "": #skips past empty items - this is protecting against an edge case, but it's an edge case that isn't impossible
            continue
        number_chunk, color_chunk = item.split(" ")
        if color_chunk in colorlimits.keys(): 
            eventValid = eventValid and (int(number_chunk) <= colorlimits[color_chunk]) #if any of them are false, output remains false for the rest of the event interpretation loop
    return eventValid

def minpossible(eventstring):
    #takes event, returns dict in order red, green, blue of minimum balls needed for the event to be possible
    list = eventstring.split(",")
    color = {'red':0, "green":0, "blue":0}
    for item in list:
        item = item.strip()
        if item=="":
            continue
        number_chunk, color_chunk = item.split(" ")
        if color_chunk in color.keys():
            color[color_chunk] += int(number_chunk)
    return color

def parse_properties(input):
    #takes string, returns dictionary with key = game ID, data = set of events
    list = input.splitlines()
    gamelist = {}
    # [id, events] = line.split(',')
    for string in list:
        id_chunk, events_chunk = string.split(":")
        events = events_chunk.split(";")
        events = [i.strip() for i in events]
        discard, id = id_chunk.split(" ")
        gamelist[id] = events
    return gamelist

def evaluategame(eventlist):
    #takes in one specific game, returns True if every event in that game was valid, and False otherwise
    gameValid = True
    for event in eventlist:
        gameValid = gameValid and interpretevent(event)
    return gameValid

def scoretally(data):
    #takes in the entire input, checks if each one is good and if so adds its ID to the tally
    score = 0
    list = parse_properties(data).items()
    for tuple in list:
        (id, game) = tuple
        if evaluategame(game):
            score += int(id)
    return score

def dictionarystitch(dict1, dict2):
    #combines two dictionaries together in a "smart" way, requires all values to be the same data type
    output = {}
    for item in dict1:
        output[item] = dict1[item]
    for item in dict2:
        if item in output:
            output[item] = max(output[item], dict2[item])
        else:
            output[item] = dict2[item]
    return output 

def powerset(eventlist):
    total = {}
    for event in eventlist:
        total.update(dictionarystitch(total, minpossible(event)))
    return total['red'] * total['green'] * total['blue']
    
def totalpower(data):
    score = 0
    list = parse_properties(data).items()
    for tuple in list:
        (discard, game) = tuple
        score += powerset(game)
    return score

class Tests(unittest.TestCase):
    def test_getproperties(self):
        assert parse_properties("") == {}
        assert parse_properties("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {"1": ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]}
    def test_interpretevents(self):
        assert interpretevent("") == True
        assert interpretevent("3 blue, 4 red") == True
        assert interpretevent("100 yellow") == True
        assert interpretevent("20 blue") == False
        assert interpretevent("20 blue, 3 red") == False

    def test_gamechecker(self):
        assert evaluategame([]) == True
        assert evaluategame(["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]) == True

    def test_minpossible(self):
        assert minpossible("3 blue, 4 red") == {'red':4, 'green':0, 'blue':3}
        assert minpossible("") == {'red':0, 'green':0, 'blue':0}

    def test_powercheck(self):
        assert powerset(["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]) == 48
        assert powerset(["1 blue, 2 green", "3 green, 4 blue, 1 red", "1 green, 1 blue"]) == 12
        assert powerset(["8 green, 6 blue, 20 red", "5 blue, 4 red, 13 green", "5 green, 1 red"]) == 1560
        assert powerset(["1 green, 3 red, 6 blue", "3 green, 6 red", "3 green, 15 blue, 14 red"]) == 630
    
    
with open("day2.txt") as f:
   data = f.read()#

if __name__ == "__main__":
    print(totalpower(data))

