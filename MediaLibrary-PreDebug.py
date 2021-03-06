#!/usr/bin/python3
# Andrew Kerr
# 1/27/2020

'''A simple module for a media library that stores games.'''

#===[ Imports ]===
import pickle

#===[ Class(es) ]===

'''MediaLibrary is a simple class that when created will read in a pickle file database of games. This will then have several helper interface functions to allow the user to interface
with the pickle file contents. This class is considered complete only after the quit method has been called doing so will effectively stop the program.'''
class MediaLibrary(object):
    
    '''SEARCH_BY_PARAMS is a static dictionary that contains the index of each search term along with a string indicating what that index is associated with.
    Used by the search_for_game method.'''
    SEARCH_BY_PARAMS = {
        0:"Genre",
        1:"Title",
        2:"Company",
        3:"Publisher",
        4:"Console",
        5:"Release Year",
        6:"Rating",
        7:"Multi/Single player",
        8:"Price",
        9:"Beaten",
        10:"Date Purchase",
    }
    
    '''Creates a new instance of the MediaLibrary class, can be supplied a filepath to the pickle file using the filepath parameter.'''
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
    
    '''This method initiates a console based user interface, once this method is called it is expected not to return as the only return point is a call to the exit method
     via the quit method.'''
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
 - 3) Search for Game
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
                self.search_for_game() 
            elif(user_selection == "4"):
                self.remove_a_game() 
            elif(user_selection == "5"):
                self.save_database() 
            elif(user_selection == "Q" or user_selection == "q"):
                self.quit()                 
            else:
                print("==============\nInvalid selection please choose from the menu.")
        print("This should never happen, your computer broke out of an infinate loop?!")
    
    '''Creates a new entry by prompting the user for information.'''
    def add_game(self):
        #for possible_key in range(self.games):
        #    if not possible_key in self.games:
        #        self.make_entry(possible_key)
        #        return
        self.make_entry(len(self.games)+1)
    
    '''Prompts the user to edit a game.'''
    def edit_game(self):
        
        finished = False
        while not finished:
            print()
            print("========================================")
            print("|     Available games for editing.     |")
            print("|       Enter nothing to return.       |")
            print("========================================")
            for key in self.games:
                print(" - "+self.games[key][1])
        
            print()
            print("========================================")
            title = input(" - Title of the game to edit: ")
            if(title == ""):
                return
            
            # Use the helper function called find_game to find a game that matches the title.
            entry_index = self.find_game(index=1,value_to_find=title)  
            if(entry_index == None):
                print("Invalid game title, please select from the list.")
            else:
                self.make_entry(entry_index)
                finished = True
                   
    '''Prompts the user for information to create a new entry.'''
    def make_entry(self,entry_index):
        
        # Begin creating a new game entry, enter a temporary while loop.
        new_entry = ["","","","","","","","","","","",""]
        valid = False
        while not valid:
        
            # Display a nice user prompt, retrieve required info for a game entry.
            print("========================================")
            new_entry[1] = input(" - Title:\t\t")
            new_entry[0] = input(" - Genre:\t\t")
            new_entry[2] = input(" - Developer:\t\t")
            new_entry[3] = input(" - Publisher:\t\t")
            new_entry[4] = input(" - Console:\t\t")
            new_entry[5] = input(" - Release Year:\t")
            new_entry[6] = input(" - Rating:\t\t")
            new_entry[7] = input(" - Multi/Single Player:\t")
            new_entry[8] = input(" - Price:\t\t")
            new_entry[9] = input(" - Have Played:\t\t")
            new_entry[10] = input(" - Date Bought:\t\t")
            new_entry[11] = input(" - Notes:\t\t")
            
            print()
            print("========================================")
            print("|  Please check the above information  |")
            print("| to make sure it is correct. [Y/N]    |")
            print("========================================")
            
            # Prompt user to make sure data is correct, exit loop if it is.
            correct = input("Is Information Correct[Y/N]: ")
            if correct.lower() in ("yes","y"):
                valid = True
                
                
        # (Re)Assign the entry at entry_index to new_entry.
        self.games[entry_index] = new_entry     
    
    '''Adds a new game to the games dictionary, or edits a previously existing entry.'''
    def add_edit_games(self):
        #print("add_edit_games method called!")
        
        finished = False
        while not finished:
            print("========================================")
            print(" - 1) Add")
            print(" - 2) Edit")
            print(" - R) Return")
            print()
            
            choice = input("What would you like to do?: ")
            choice = choice.lower()
            
            if choice == "1":
                self.add_game()
            elif choice == "2":
                self.edit_game()
            elif choice == "r":
                finished = True
            else:
                print("Please select a valid choice!")
                print()

    '''
    Searches through the games dictionary for the first game that has a value matching the value_to_find using the index.
    
    Parameters:
     - index: (default 0), Index of the value were searching for.
     - value_to_find: (default ""), The value to find.
     
    Returns:
     - Either a key of the game that matched or a None type object.
    '''
    def find_game(self,index=0,value_to_find=""):
        for key in self.games:
            game = self.games[key]
            if value_to_find.lower() == game[index].lower():
                return key
        return None
    
    '''
    Searches through the games dictionary for any games that have a value matching the value_to_find using the index.
    
    Parameters:
     - index: (default 0), Index of the value were searching for.
     - value_to_find: (default ""), The value to find.
     
    Returns:
     - A list containing the keys of any games that matched the search, can be of size 0.
    '''    
    def find_games(self,index=0,value_to_find=""):
        result = []
        for key in self.games:
            game = self.games[key]
            if value_to_find.lower() in game[index].lower():
                result.append(key)
        return result        
      
    '''
    Prints all of the games found within the games dictionary.
    
    Returns:
     - Nothing
    '''
    def print_all_games(self):
        #print("print_all_games method called!")
        for key in self.games:
            game = self.games[key]
            self.print_game(game)
    
    '''
    Prints a single game out to the console, requires a list of length 12 be passed.
    
    Parameters:
     - game: A list containing all of the necessary information for a game entry.
     
    Returns:
     - Nothing
    '''
    def print_game(self,game):
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

    '''
    Retrieves a search term from the user before attempting to search through the games dictionary for any possible matches.
    '''
    def search_for_game(self):
        #print("search_for_game method called!")
        
        #Grab search term list from master copy.
        search_terms = MediaLibrary.SEARCH_BY_PARAMS
        
        #Enter a secondary while loop for searching.
        while True:
            
            #Print out all search by terms and their index's.
            print("========================================")
            print("|   Search using one of the following  |")
            print("|     search terms, enter the number   |")
            print("|         below or 'e' to exit.        |")
            print("========================================")
            for index in search_terms:
                print(" - "+str(index)+") "+search_terms[index])
            print("========================================")
            
            #Retrieve the index of the program.
            search_by = input(" - Search by: ")
            print("========================================")
            print()
            
            #Check if user wishes to exit.
            if(search_by.lower() == 'e'):
                break
            
            #Attempt to convert search_by into an integer and assign it to index.
            try:
                index = int(search_by)
                
                #Invalid number, Restart loop due to invalid index.
                if not(index in search_terms):
                    print("========================================")
                    print("- Invalid search term, please try again.")
                    print("========================================")
                    continue
            except: # Restart loop due to a invalid conversion to integer.
                print("========================================")
                print("- Invalid search term, please use a number")
                print("========================================")
                print()
                continue
            
            #Retrieve the term to search by, ie: Genre, Title, etc.
            term = search_terms[index]
            
            print("========================================")
            search_value = input(" - "+term+" of desired game(s): ")
            print("========================================")
            for key in self.find_games(index=index,value_to_find=search_value):
                self.print_game(self.games[key])
        
    
    '''Removes a game from the games dictionary.'''
    def remove_a_game(self):
        #print("remove_a_game method called!")
        valid = False
        while not valid:
            print("""
========================================
|         Remove a Game Entry          |
|       Enter nothing to return.       |
========================================
""")
            for key in self.games:
                print(" - "+str(key)+") "+self.games[key][1])
            
            print()
            selected_key = input("What would you like to remove?: ")
            
            if selected_key == "":
                return
            
            try:
                selected_key = int(selected_key)
            except:
                print()
                print("========================================")
                print("|Invalid input, please supply a number.|")
                print("========================================")
                continue
            
            if not selected_key in self.games:
                print()
                print("========================================")
                print("|Invalid input, selection isnt in range|")
                print("========================================")
                continue
            
            self.games.pop(selected_key)
            valid = True
    
    '''Saves the games dictionary to the pickle file.'''
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
        
    '''Exits the program'''
    def quit(self):
        #print("quit method called!\nExiting now!")
        print("""
========================================
| Would you like to quit the program?  |
========================================""")
        
        user_wishes_quit = input("Quit? [Y/N]: ")
        if not user_wishes_quit.lower() == "y":
            return
        
        print("""
========================================
| Would you like to save any changes?  |
========================================""")
        
        user_wishes_save = input("Save? [Y/N]: ")
        if user_wishes_save.lower() == "y":
            self.save_database()
        
        print("""
========================================
| Exiting program, Goodbye!            |
========================================""")
        exit()
        
if( __name__ == "__main__" ):
    media_library = MediaLibrary()
    media_library.mainloop()