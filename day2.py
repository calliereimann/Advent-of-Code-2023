import unittest

colorlimits = {'red': 12, 'green':13, 'blue':14} #number of balls of each color

def interpretevent(string):
    #takes event, returns true if all values are within the limits
    list = string.split(",")
    output=True
    for item in list:
        item = item.strip()
        number_chunk, color_chunk = item.split(" ")
        if color_chunk in colorlimits.keys():
            output = output and (number_chunk <= colorlimits[color_chunk])
    return output

    

def parse_properties(input):
    #takes string, returns game ID, set of events
    list = input.splitlines()
    output = {}
    # [id, events] = line.split(',')
    for string in list:
        id_chunk, events_chunk = string.split(":")
        events = events_chunk.split(";")
        for item in events:
            item = item.strip()
        discard, id = id_chunk.split(" ")
        output[id] = events
    return output

    
class Tests(unittest.TestCase):
    def test_getproperties(self):
        assert parse_properties("") == {}
        print(parse_properties("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
        assert parse_properties("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == {"1": ["3 blue, 4 red", "1 red, 2 green, 6 blue", "2 green"]}
    

