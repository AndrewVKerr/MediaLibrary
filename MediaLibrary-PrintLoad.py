#!/usr/bin/python3
# Andrew Kerr
# 1/27/2020

'''A simple module for a media library that stores games.'''

import pickle

class MediaLibrary(object):
    
    def __init__(self,filepath="game_lib.pickle"):
        try:
            self.filepath = filepath
            datafile = open(filepath,"rb")
            self.games = pickle.load(datafile)
            datafile.close()
        except Exception as e:
            print("\t================================")
            print("\t - Failed to open picklefile! - ")
            print("\t================================")
            raise e
    
    def mainloop(self):
        # Found an interesting thing, functions are basically callable variables. They are stored much the same way as variables. This allows for you to store them
        #  in a dictionary like so and still be able to call them later. The way you call them is much the same except now they are stored under a differnt variable name or called directly.
        # EX: selectables["1"]() or action = selectables["2"] \n action().
        # https://softwareengineering.stackexchange.com/questions/182093/why-store-a-function-inside-a-python-dictionary/182095
        #selectables = {
        #    "1":self.add_edit_games, 
        #    "2":self.print_all_games,
        #    "3":self.search_by_title,
        #    "4":self.remove_a_game,
        #    "5":self.save_database,
        #    "Q":self.quit
        #}
        
        while(True):
            print('''
========[ MediaLibrary | Main Menu ]========
 - 1) Add/Edit Game
 - 2) Print All Games
 - 3) Search by Title
 - 4) Remove a Game
 - 5) Save Database
 - Q) Quit
''')
            user_selection = input("Please choose a number from the menu above: ")
            if(user_selection == "1"):
                self.add_edit_games()
            elif(user_selection == "2"):
                self.print_all_games() 
            elif(user_selection == "3"):
                self.search_by_title() 
            elif(user_selection == "4"):
                self.remove_a_game() 
            elif(user_selection == "5"):
                self.save_database() 
            elif(user_selection == "Q" or user_selection == "q"):
                self.quit()                 
            else:
                print("==============\nInvalid selection please choose from the menu.")
        print("This should never happen, your computer broke out of an infinate loop?!")
        
    def add_edit_games(self):
        print("add_edit_games method called!")
        
    def print_all_games(self):
        #print("print_all_games method called!")
        for key in self.games:
            game = self.games[key]
            print("""
========================================
 - Title:\t\t"""+game[1]+"""
 - Genre:\t\t"""+game[0]+"""
 - Developer:\t\t"""+game[2]+"""
 - Publisher:\t\t"""+game[3]+"""
 - Console:\t\t"""+game[4]+"""
 - Release Year:\t"""+game[5]+"""
 - Rating:\t\t"""+game[6]+"""
 - Multi/Single Player:\t"""+game[7]+"""
 - Price:\t\t"""+game[8]+"""
 - Have Played:\t\t"""+game[9]+"""
 - Date Bought:\t\t"""+game[10]+"""
 - Notes:\t\t"""+game[11]+"""

""")

    def search_by_title(self):
        print("search_by_title method called!")
        
    def remove_a_game(self):
        print("remove_a_game method called!")
    
    def save_database(self):
        #print("save_database method called!")    
        datafile = open(self.filepath,"wb")
        pickle.dump(self.games,datafile)
        datafile.close()
        print("""
========================================
 - Saved database to file. 
   ["""+self.filepath+"""]
========================================
""")
        
    def quit(self):
        print("quit method called!\nExiting now!")
        exit()
        
if( __name__ == "__main__" ):
    media_library = MediaLibrary()
    media_library.mainloop()