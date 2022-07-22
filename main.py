import pickle

with open(r"C:\Users\silve\OneDrive\Documents\Repos\wordle-world\big_city_list", "rb") as f:
    all_cities = pickle.load(f)

with open(r"C:\Users\silve\OneDrive\Documents\Repos\wordle-world\guess_city_list", "rb") as f:
    guess_cities = pickle.load(f)

print(guess_cities[5], all_cities[100])