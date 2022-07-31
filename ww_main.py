import pickle
import random
import os
import tkinter
import tkinter.messagebox

dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, 'big_city_list'), "rb") as f:
    all_cities = pickle.load(f)

with open(os.path.join(dirname, 'guess_city_list'), "rb") as f:
    guess_cities = pickle.load(f)

random.shuffle(guess_cities)

# build the game engine
# each game will be a new object

class Game:
    '''this object holds the answer to the game and will return information on what part of a guess is correct when the guess function is called.
       must be passed a tuple from guess_cities'''
    def __init__(self, guess_city):
        self.answer_string = guess_city[1].upper()
        self.answer_country = guess_city[0]
    
    def guess(self, city):
        '''city must be a string. return object will be a list of 6 values representing the 6 characters in the guess.
        0 is not present, 1 is present in a different position, and 2 is present in correct position'''
        return_list = []
        index = 0
        for char in city:
            if char.upper() == self.answer_string[index].upper():
                return_list.append(2)
                index += 1
            elif char.upper() in self.answer_string:
                return_list.append(1)
                index += 1
            else:
                return_list.append(0)
                index += 1

        return return_list

# this section contains the GUI and running code

class ProgramGUI:
    def __init__(self):
        self.main = tkinter.Tk()
        self.main.title('Wordle World')

        # create 36 StringVar, one for each of the entries
        self.var_list = []
        for i in range(1,7):
            for j in range(1,7):
                self.var_list.append(str(i) + str(j))
        self.var_dict = {var: tkinter.StringVar() for var in self.var_list}

        # main row frames
        self.title_row = tkinter.Frame(self.main)
        self.instruction_row = tkinter.Frame(self.main)
        self.row1 = tkinter.Frame(self.main)
        self.row2 = tkinter.Frame(self.main)
        self.row3 = tkinter.Frame(self.main)
        self.row4 = tkinter.Frame(self.main)
        self.row5 = tkinter.Frame(self.main)
        self.row6 = tkinter.Frame(self.main)
        self.keyboard_row = tkinter.Frame(self.main)
        self.buttons_row = tkinter.Frame(self.main)

        # title frame
        self.title_label = tkinter.Label(self.title_row, text='Wordle World', font='Calibri 20 bold').pack(side='top')
        self.instruction_label = tkinter.Label(self.instruction_row, text='Like Wordle, but with 6 letter cities of the world!', font='Calibri 14 bold').pack(side='top')

        # going to use zip to create a dictionary of entry boxes and rows. There are 6 entry boxes per row, so to use zip need to create a list with each row x6
        self.row_list = [self.row1, self.row2, self.row3, self.row4, self.row5, self.row6]

        self.row_list_exp = []
        for row in self.row_list:
            for num in range(6):
                self.row_list_exp.append(row)

        # code to use this row and variable list to pack fresh entry widgets has been abstracted to this function
        self.new_game()
        
        # add on-screen keyboard code here

        # create and pack buttons
        self.submit_button = tkinter.Button(self.buttons_row, text='Submit', font='Calibri 16 bold', command=lambda: self.guess()).pack(side='left', padx='15')
        self.new_button = tkinter.Button(self.buttons_row, text='New Game', font='Calibri 16 bold', command=lambda: self.new_game()).pack(side='left', padx='15')
        
        # pack frames
        self.title_row.pack()
        self.instruction_row.pack(padx='5', pady='5')
        self.row1.pack()
        self.row2.pack()
        self.row3.pack()
        self.row4.pack()
        self.row5.pack()
        self.row6.pack()
        self.keyboard_row.pack()
        self.buttons_row.pack(padx='10', pady='10')
        
        tkinter.mainloop()

    # placeholder function for button - remove once real function is created
    def placeholder_function(self):
        pass

    def create_entries(self):
        '''this function creates and packs the entry widgets'''
        # create a dictionary of 36 tkinter.Entry for the letter entry boxes. first digit is row, second digit is position. eg 11 (top left) to 66 (bottom right)
        self.entry_dict = {var: tkinter.Entry(row, width='3', textvariable=self.var_dict[var], font='Calibri 14', justify='center') 
                            for var, row in zip(self.var_list, self.row_list_exp)}
        
        # pack entry widgets
        for var in self.var_list:
            self.entry_dict[var].pack(side='left', padx='1', pady='1')

        # disable entry boxes from line 2 onwards
        for var_name in self.var_list[6:]:
            self.entry_dict[var_name].config(state = 'disabled')

    def new_game(self):
        ''' resets the gui and creates a new game'''
        for row in self.row_list:
            for widget in row.winfo_children():
                widget.destroy()

        self.var_dict = {var: tkinter.StringVar() for var in self.var_list}
        
        self.guesses = 0
        self.game = Game(guess_cities.pop())

        self.create_entries()

    # add some error checking / exception handling here
    def guess(self):
        ''' this function submits the guess and moves the game to the next line'''
        guess_char_list = []
        for entry in self.row_list[self.guesses].winfo_children():
            guess_char_list.append(entry.get().upper())

        return_values = self.game.guess(guess_char_list)
        
        # destroy the frames in the row, and replace with labels with guess letters of the correct colour
        for entry in self.row_list[self.guesses].winfo_children():
            entry.destroy()

        row_label_dict = {}
        for letter, result, index in zip(guess_char_list, return_values, range(6)):
            if result == 0:
                colour = 'Red'
            elif result == 1:
                colour = 'Yellow'
            else:
                colour = 'Green'

            row_label_dict[index] =  tkinter.Label(self.row_list[self.guesses], text=letter.upper(), font='Calibri 14 bold', bg=colour)
      
        for num in range(6):
            row_label_dict[num].pack(side='left', padx='10', pady='1')

        for var_name in self.var_list[((self.guesses + 1) * 6):((self.guesses + 2) * 6)]:
            self.entry_dict[var_name].config(state = 'normal')

        self.guesses += 1   

        if return_values == [2, 2, 2, 2, 2, 2]:
            tkinter.messagebox.showinfo('Congratulations!', 'You solved it! '+ self.game.answer_string.title() + ' is the capital of '+ self.game.answer_country + '.')
        
        elif self.guesses == 6:
            tkinter.messagebox.showerror('Out of Guesses!', 'You ran out of guesses without solving it. The answer was ' + self.game.answer_string.title() + ', capital of ' + self.game.answer_country + '.')


gui = ProgramGUI()