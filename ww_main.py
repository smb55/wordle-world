# to do:
# set cursor to first box
# implement keyboard functions to actually press the key
# make boxes bigger to match keyboard size (or keyboard smaller)

import pickle
import random
import os
import sys
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkm

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
        self.answer_string = ''
        for char in guess_city:
            self.answer_string += char.upper()
    
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
        self.main = tk.Tk()
        self.main.title('Wordle World')

        # create 36 StringVar, one for each of the entries
        self.var_list = []
        for i in range(1,7):
            for j in range(1,7):
                self.var_list.append(str(i) + str(j))
        self.var_dict = {var: tk.StringVar() for var in self.var_list}

        # main row frames
        self.title_row = tk.Frame(self.main)
        self.instruction_row = tk.Frame(self.main)
        self.row1 = tk.Frame(self.main)
        self.row2 = tk.Frame(self.main)
        self.row3 = tk.Frame(self.main)
        self.row4 = tk.Frame(self.main)
        self.row5 = tk.Frame(self.main)
        self.row6 = tk.Frame(self.main)
        self.keyboard_row = tk.Frame(self.main)
        self.buttons_row = tk.Frame(self.main)

        # title frame
        self.title_label = tk.Label(self.title_row, text='Wordle World', font='Calibri 20 bold').pack(side='top')
        self.instruction_label = tk.Label(self.instruction_row, text='Like Wordle, but with 6 letter cities of the world!', font='Calibri 14 bold').pack(side='top')

        # keyboard frame
        self.key = tk.Frame(self.keyboard_row)

        ## On-screen keyboad not yet working so is commented out
        
        # # First Line Button
        
        # q = ttk.Button(self.key,text = 'Q' , width = 6, command = lambda : self.press('Q'))
        # q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)
        
        # w = ttk.Button(self.key,text = 'W' , width = 6, command = lambda : self.press('W'))
        # w.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)
        
        # E = ttk.Button(self.key,text = 'E' , width = 6, command = lambda : self.press('E'))
        # E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)
        
        # R = ttk.Button(self.key,text = 'R' , width = 6, command = lambda : self.press('R'))
        # R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)
        
        # T = ttk.Button(self.key,text = 'T' , width = 6, command = lambda : self.press('T'))
        # T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)
        
        # Y = ttk.Button(self.key,text = 'Y' , width = 6, command = lambda : self.press('Y'))
        # Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)
        
        # U = ttk.Button(self.key,text = 'U' , width = 6, command = lambda : self.press('U'))
        # U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)
        
        # I = ttk.Button(self.key,text = 'I' , width = 6, command = lambda : self.press('I'))
        # I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)
        
        # O = ttk.Button(self.key,text = 'O' , width = 6, command = lambda : self.press('O'))
        # O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)
        
        # P = ttk.Button(self.key,text = 'P' , width = 6, command = lambda : self.press('P'))
        # P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)
               
        # # Second Line Button       
        # A = ttk.Button(self.key,text = 'A' , width = 6, command = lambda : self.press('A'))
        # A.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)
                        
        # S = ttk.Button(self.key,text = 'S' , width = 6, command = lambda : self.press('S'))
        # S.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)
        
        # D = ttk.Button(self.key,text = 'D' , width = 6, command = lambda : self.press('D'))
        # D.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)
        
        # F = ttk.Button(self.key,text = 'F' , width = 6, command = lambda : self.press('F'))
        # F.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)
               
        # G = ttk.Button(self.key,text = 'G' , width = 6, command = lambda : self.press('G'))
        # G.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)
               
        # H = ttk.Button(self.key,text = 'H' , width = 6, command = lambda : self.press('H'))
        # H.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)
                
        # J = ttk.Button(self.key,text = 'J' , width = 6, command = lambda : self.press('J'))
        # J.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)
                
        # K = ttk.Button(self.key,text = 'K' , width = 6, command = lambda : self.press('K'))

        # K.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)
        
        # L = ttk.Button(self.key,text = 'L' , width = 6, command = lambda : self.press('L'))
        # L.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)
               
        # # third line Button        
        # Z = ttk.Button(self.key,text = 'Z' , width = 6, command = lambda : self.press('Z'))
        # Z.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)
          
        # X = ttk.Button(self.key,text = 'X' , width = 6, command = lambda : self.press('X'))
        # X.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)
            
        # C = ttk.Button(self.key,text = 'C' , width = 6, command = lambda : self.press('C'))
        # C.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)
               
        # V = ttk.Button(self.key,text = 'V' , width = 6, command = lambda : self.press('V'))
        # V.grid(row = 3 , column = 4, ipadx = 6 , ipady = 10)
       
        # B = ttk.Button(self.key, text= 'B' , width = 6 , command = lambda : self.press('B'))
        # B.grid(row = 3 , column = 5 , ipadx = 6 ,ipady = 10)
      
        # N = ttk.Button(self.key,text = 'N' , width = 6, command = lambda : self.press('N'))
        # N.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)
                
        # M = ttk.Button(self.key,text = 'M' , width = 6, command = lambda : self.press('M'))
        # M.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)

        # self.clear_button = ttk.Button(self.key,text = 'Clear', width = 6, command = lambda : self.clear())
        # self.clear_button.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)

        # self.key.pack(padx=10, pady=10)

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
        self.submit_button = tk.Button(self.buttons_row, text='Submit', font='Calibri 16 bold', command=lambda: self.guess()).pack(side='left', padx='15')
        self.new_button = tk.Button(self.buttons_row, text='New Game', font='Calibri 16 bold', command=lambda: self.new_game()).pack(side='left', padx='15')
        
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
        
        tk.mainloop()

    # On screen keyboard functions

    ##### Need to fix this function
    
    # key self.press function
    def press(self, char):
        pass
    
        #sys.stdin.write(char)
        #sys.stdin.write('\t')
    
    # self.clear button function 
    def clear():
        # add code here
        pass

    def create_entries(self):
        '''this function creates and packs the entry widgets'''
        # create a dictionary of 36 tk.Entry for the letter entry boxes. first digit is row, second digit is position. eg 11 (top left) to 66 (bottom right)
        self.entry_dict = {var: tk.Entry(row, width='3', textvariable=self.var_dict[var], font='Calibri 14', justify='center') 
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

        self.var_dict = {var: tk.StringVar() for var in self.var_list}
        
        self.guesses = 0
        self.game = Game(guess_cities.pop())

        self.create_entries()

        # set focus to the first box
        self.entry_dict['11'].focus_set()

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

            row_label_dict[index] =  tk.Label(self.row_list[self.guesses], text=letter.upper(), font='Calibri 14 bold', bg=colour)
      
        for num in range(6):
            row_label_dict[num].pack(side='left', padx='10', pady='1')

        for var_name in self.var_list[((self.guesses + 1) * 6):((self.guesses + 2) * 6)]:
            self.entry_dict[var_name].config(state = 'normal')

        self.guesses += 1   

        if return_values == [2, 2, 2, 2, 2, 2]:
            tkm.showinfo('Congratulations!', 'You solved it!')
        
        elif self.guesses == 6:
            tkm.showerror('Out of Guesses!', 'You ran out of guesses without solving it. The answer was ' + self.game.answer_string.title())


gui = ProgramGUI()