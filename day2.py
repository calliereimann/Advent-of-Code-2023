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
    
if __name__ == '__main__':
    unittest.main()

