import pickle
import random

with open(r"C:\Users\silve\OneDrive\Documents\Repos\wordle-world\big_city_list", "rb") as f:
    all_cities = pickle.load(f)

with open(r"C:\Users\silve\OneDrive\Documents\Repos\wordle-world\guess_city_list", "rb") as f:
    guess_cities = pickle.load(f)

random.shuffle(guess_cities)

# build the game engine
# each game will be a new object

class Game:
    '''this object holds the answer to the game and will return information on what part of a guess is correct when the guess function is called'''
    def __init__(self, answer_city):
        self.answer_string = answer_city
    
    def guess(self, city):
        '''city must be a string. return object will be a list of 6 values representing the 6 characters in the guess.
        0 is not present, 1 is present in a different position, and 3 is present in correct position'''
        return_list = []
        index = 0
        for char in city:
            if char.lower() == self.answer_string[index].lower():
                return_list.append(2)
                index += 1
            elif char.lower() in self.answer_string:
                return_list.append(1)
                index += 1
            else:
                return_list.append(0)
                index += 1

        return return_list
