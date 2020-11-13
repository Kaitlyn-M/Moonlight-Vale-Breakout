#Imports a custom "classes" module.
import classes

#Displays a custom death message.
def dead(death_msg):
    
    #Prints the custom death message.
    print(death_msg)

#Introduces the game to the user.
def intro():
    
    #Prints the game's title.
    print("\n\n\t-~* Welcome to Moonlight Vale: Breakout! *~-\n")

    #Provides the game's description and player instructions.
    print("Your character is locked in an insane asylum (Moonlight Vale).")
    print("Goal: Successfully escape Moonlight Vale.")
    print("Read the story and decide your character's actions.")
    print("Throughout the game, you can obtain and/or use items.")
    print("Once an item is used, it is no longer in your inventory.")
    print("Based on the item you pick up, you will earn a certain amount of points.")
    print("Candy = 5 points. Keycard = 5 points. Potion = 10 points. Blade = 15 points.")
    print("Your character may die in the process.")
    print("The likeliness of death is based on the game's difficulty.")
    print("Here are your difficulty choices:")
    print("'Surface' for easy. 'Underground' for medium. 'Hell' for hard.")

    #User can choose the game's difficulty.
    #lower() makes the input not case sensitive.
    difficulty = input("\nChoose the game's difficulty: ").lower()

    #Returns the chosen difficulty for other functions to use.
    return difficulty

#Driver function for all other functions.
def main():

    #The user will continue playing.
    continue_game = True

    #Executes while continue_game is true.
    while continue_game == True:

        #The game's difficulty is based on the user's choice in intro().
        difficulty = intro()

        #If the user chooses the easy difficulty.
        if difficulty == "surface":
        
            #Character menu. User can create a new character or use an existing character.
            menu()

            #Creates a "game" object that is set to the surface difficulty.
            game = classes.Surface()

            #Introduces the patient as "surface" level.
            game.story_intro()

            #Sets the user inventory to the return value of the inventory function.
            user_inv = game.inventory()

            #The easy game.
            game.surface(user_inv)

        #If the user chooses the medium difficulty.
        elif difficulty == "underground":
                   
            #Character menu. User can create a new character or use an existing character.
            menu()

            #Creates a "game" object that is set to the underground difficulty.
            game = classes.Underground()

            #Introduces the patient as "underground" level.
            game.story_intro()

            #Sets the user inventory to the return value of the inventory function.
            user_inv = game.inventory()

            #The medium game.
            game.underground(user_inv)

        #If the user chooses the hard difficulty.
        elif difficulty == "hell":
                   
            #Character menu. User can create a new character or use an existing character.
            menu()
            
            #Creates a "game" object that is set to the hell difficulty.
            game = classes.Hell()

            #Introduces the patient as "hell" level.
            game.story_intro()

            #Sets the user inventory to the return value of the inventory function.
            user_inv = game.inventory()

            #The hard game.
            game.hell(user_inv)

        #If the user does not choose a difficulty.
        else:
            
            dead("\nAt least choose a difficulty...sheesh...")

        #Asks the user if they would like to play again.
        #lower() makes the input not case-sensitive.
        user_play = input("\nWould you like to play again? (yes/no): ").lower()
        
        #Executes if the user chooses "yes".
        if user_play == "yes":
            
            #Allows the user to play again.
            continue_game = True
        
        #Executes if the user chooses "no".
        elif user_play == "no":
            
            #Allows the user to end the program.
            continue_game = False
        
        #Executes if the user does not choose "yes" or "no".
        else:
            
            #Loops while user does not choose "yes" or "no".
            while user_play != "yes" and user_play != "no":
                
                #Asks the user if they would like to play again.
                #lower() makes the input not case-sensitive.
                user_play = input("\nWould you like to play again? (yes/no): ").lower()

#Character menu. User can create a new character or use an existing character.
def menu():
    
    #Indicates the character menu.
    print("\n\n----- CHARACTER MENU -----")

    #User can choose to create a new character or use an existing character.
    #lower() makes the input not case sensitive.
    new_or_exist = input("\nChoose whether you want to create a 'new' character or use an 'existing' character: ").lower()

    #Executes if the user chooses "new".
    if new_or_exist == "new":

        #Writes user input to the file.
        write_file()
    
    #Executes if the user chooses "existing".
    elif new_or_exist == "existing":
        
        #Reads from the file.
        read_file()

    #Executes if the user doesn't choose "new" or "existing".
    else:
        
        dead("\nC'mon, you couldn't even determine if you wanted a new or existing character...\n")
        
        #Exits the program.
        exit(0)

#Reads text from the file.
def read_file():
    
    #Opens a file handle that's in read mode.
    file_handle = open("characters.txt", "r")

    #Allows user to input an existing character name.
    character_name = input("\nEnter an existing character's name (case sensitive): ")

    #Reads the entire file then puts everything in file_contents.
    file_contents = file_handle.read()

    #Executes if character_name is found in file_contents.
    if character_name in file_contents:

        #Greets the character.
        print(f"Hello, {character_name}! Transferring you to the game...\n")

    #Executes if character_name is not found in file_contents.
    else:
        
        dead("\nCharacter was not found. Ending program...\n")
        
        #Exits the program.
        exit(0)

    #Closes the file handle.
    file_handle.close()

#Writes user input to the file.
def write_file():
    
    #Opens a file handle that's in append mode.
    #Append mode allows multiple characters to be stored in the same file.
    file_handle = open("characters.txt", "a")

    #Prompts user to enter the character's name.
    character_name = input("\nEnter your character's name: ")

    #Adds character name to the file.
    file_handle.write(character_name + "\n")

    # Closes the file handle.
    file_handle.close()
