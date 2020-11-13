#Imports a custom "functions" module.
import functions
#Imports the random module.
import random

#Difficulty class that all difficulties inherit from.
class Difficulty:
    
    #Constuctor of the Difficulty class.
    def __init__(self, difficulty):
        
        #Sets the object's difficulty.
        self.difficulty = difficulty
    
    #Creates and indicates an empty inventory.
    def inventory(self):
    
        #Creates an empty inventory.
        user_inv = ['']
        #Indicates an empty inventory.
        print("\nAn empty inventory has been created.")

        #Returns user_inv for other functions to use.
        return user_inv

    #Inventory at the end of the game.
    def inv_final(self, user_inv2, inv_points):
   
        #Removes empty strings.
        user_inv2.remove('')
        #Indicates what the user escaped with.
        print("\nYou escaped with..." + ', '.join(user_inv2) + ".")
        
        print(f"You successfully escaped the asylum with {inv_points} points!")

    #Introduces the story based on the user's difficulty.
    def story_intro(self):
        
        print(f"\n\nHave fun playing as a(n) {self.difficulty} patient!")

#Hell (hard) difficulty class.
class Hell(Difficulty):
    
    #Constuctor of the Hell class.
    def __init__(self):
        
        #Inherits from the Difficulty class and sets "Hell" as the difficulty.
        super().__init__("Hell")

    #Part 1 of hard difficulty's gameplay.
    def hell(self, user_inv):

        #Stores points based on the value and amount of inventory items the character has.
        inv_points = 0
        
        #The hard situation.
        print("\n\nWell, this is going to be tough.")
        print("You have to go through two elevators and fight half a dozen guards off.")
        print("Do you decide to wait for a staff member to release you or get out on your own?")
        
        #The user can choose to 'wait' or 'go'.
        #lower() makes the input not case-sensitive.
        wait_or_go = input("\nChoose 'wait' or 'go': ").lower()

        #Executes if the user chose "wait".
        if wait_or_go == "wait": 

            functions.dead("\nNo one trusted you enough to open the cell so you were left to rot.")

        #Executes if the user chose "go".
        elif wait_or_go == "go":
            
            #Indicates a keycard.
            print("\nYou notice a keycard then decide to pick it up.")
            #Appends/adds the keycard to the inventory.
            user_inv.append("keycard")

            #Adds 5 points to total points for obtaining a keycard.
            inv_points += 5

            #Asks the user if they will use or keep the keycard.
            #lower() makes the input not case-sensitive.
            use_or_keep = input("Do you use or keep the keycard?: ").lower()


            #If the user chooses "use".
            if use_or_keep == "use":
                
                #Indicates keycard use.
                print("\nYou used the keycard to exit the cell.")
                #Removes keycard from the list.
                user_inv.remove("keycard")

                #Subtracts 5 points from total points for using the keycard.
                inv_points -= 5

                #Current inventory is transferred to part two's inventory.
                user_inv2 = user_inv

                #Part 2 of the story.
                self.hell_p2(user_inv2, inv_points)

            #If the user chooses "keep".
            elif use_or_keep == "keep":
                
                #Indicates strength use.
                print("\nYou used your strength to exit the cell.")

                #Current inventory is transferred to part two's inventory.
                user_inv2 = user_inv

                #Part 2 of the story.
                self.hell_p2(user_inv2, inv_points)

            #If the user does not choose "use" or "keep".
            else:
                functions.dead("\nYou were too indecisive.")

        #Executes if the user does not choose "wait" or "go".
        else:
            
            functions.dead("\nYour character died at a lost opportunity.")

    #Part 2 of hard difficulty's gameplay.
    def hell_p2(self, user_inv2, inv_points):
        
        #The story continues.
        print("\nAs you run off, there are six guards chasing you.")
        print("While you run away, you notice a potion and blade.")
        print("You pick both items up.")
        
        #Adds potion and blade to the user's inventory.
        user_inv2.extend(("potion", "blade"))

        #Adds 25 points to total points for obtaining potion and blade.
        inv_points += 25

        #User can choose which item to use for escape.
        #lower() makes the input not case-sensitive.
        item_use = input("\nChoose which item to use in your escape: ").lower()

        #If the user chooses "potion"
        if item_use == "potion":
            
            #Stores a random number from 0 to 100.
            rdm_potion_num = random.randint(0, 100)

            #Indicates RNG (random number generator).
            print(f"\nLet's see how effective the potion is via RNG: {rdm_potion_num}")

            #Subtracts 10 from total points for using potion.
            inv_points -= 10

            #If the random potion number is less than 60, the character dies.
            if rdm_potion_num < 60:
                
                functions.dead("Your character died because the potion was too strong.")
            
            #If the random number is greater than or equal to 60, the character escapes.
            else:
                    
                print("The potion strengthed your body!")

                #Removes potion from the user's inventory.
                user_inv2.remove("potion")
                
                #Displays the final inventory.
                self.inv_final(user_inv2, inv_points)

        #If the user chooses "blade"
        elif item_use == "blade":
        
            #Stores a random number from 0 to 100.
            rdm_num = random.randint(0, 100)

            #Indicates RNG (random number generator).
            print(f"\nLet's see how effective the blade is via RNG: {rdm_num}")

            #Subtracts 15 from total points for using potion.
            inv_points -= 15

            # If the random number is less than 75, the character dies.
            if rdm_num < 75:

                functions.dead("\nYour escape attempt failed and got you killed.")
            
            # If the random number is greater than or equal to 75, the character escapes.
            else:
                
                #Removes blade from the user's inventory.
                user_inv2.remove("blade")
                
                #Displays the final inventory.
                self.inv_final(user_inv2, inv_points)

        #Displays a death message.
        else:
            
            functions.dead("You should've just used one to help you escape...")

#Surface (easy) difficulty class.
class Surface(Difficulty):
    
    #Constuctor of the Surface class.
    def __init__(self):
        
        #Inherits from the Difficulty class and sets "Surface" as the difficulty.
        super().__init__("Surface")

    #Part 1 of easy difficulty's gameplay.
    def surface(self, user_inv):

        #Stores points based on the value and amount of inventory items the character has.
        inv_points = 0

        #The easy situation.
        print("\n\nLuckily for you, the exit is close by.")
        print("All your character has to do is get out of the cell and run across the hall.")
        print("Do you decide to wait for a staff member to release you or get out on your own?")
        
        #The user can choose to 'wait' or 'go'.
        #lower() makes the input not case-sensitive.
        wait_or_go = input("\nChoose 'wait' or 'go': ").lower()

        #Executes if the user chose "wait".
        if wait_or_go == "wait": 
            
            #Indicates success and the user can proceed.
            print("\nIt didn't take long before a staff member released you from your cell.")
            print("Since you're trustworthy enough, you could be in the cafeteria without much supervision.")
            print("You're such a great patient that you were given a piece of candy.")

            #Adds candy to the inventory.
            user_inv.append("candy")
            
            #Adds 5 points to total for obtaining candy.
            inv_points += 5

            #Current inventory is transferred to part two's inventory.
            user_inv2 = user_inv

            #Part 2 of the story.
            self.surface_p2(user_inv2, inv_points)
    
        #Executes if the user chose "go".
        elif wait_or_go == "go":
            
            functions.dead("\nThat was not the best option...considering your character is pretty weak...")

        #Executes if the user does not choose "wait" or "go".
        else:
            
            functions.dead("\nYour character died at a lost opportunity.")

    #Part 2 of easy difficulty's gameplay.
    def surface_p2(self, user_inv2, inv_points):
        
        #The story continues.
        print("\nAfter you take the candy, you run away.")
        print("While you run away, you notice a potion and blade.")
        print("You pick both items up.")
        
        #Adds potion and blade to the user's inventory.
        user_inv2.extend(("potion", "blade"))

        #Adds 25 points to total points for obtaining potion and blade.
        inv_points += 25

        #User can choose which item to use for escape.
        #lower() makes the input not case-sensitive.
        item_use = input("\nChoose which item to use in your escape: ").lower()

        #If the user chooses "potion"
        if item_use == "potion":
            
            #Stores a random number from 0 to 100.
            rdm_potion_num = random.randint(0, 100)

            #Indicates RNG (random number generator).
            print(f"\nLet's see how effective the potion is via RNG: {rdm_potion_num}")

            #Subtracts 10 from total points for using potion.
            inv_points -= 10

            #If the random potion number is less than 20, the character dies.
            if rdm_potion_num < 20:
                
                functions.dead("Your character died because the potion was too strong.")
            
            #If the random number is greater than or equal to 20, the character escapes.
            else:
                    
                print("The potion strengthed your body!")

                #Removes potion from the user's inventory.
                user_inv2.remove("potion")
                
                #Displays the final inventory.
                self.inv_final(user_inv2, inv_points)

        #If the user chooses "blade"
        elif item_use == "blade":
        
            #Stores a random number from 0 to 100.
            rdm_num = random.randint(0, 100)

            #Indicates RNG (random number generator).
            print(f"\nLet's see how effective the blade is via RNG: {rdm_num}")

            #Subtracts 15 from total points for using blade.
            inv_points -= 15

            #If the random number is less than 25, the character dies.
            if rdm_num < 25:

                functions.dead("\nYour escape attempt failed and got you killed.")
            
            #If the random number is greater than or equal to 25, the character escapes.
            else:
                
                #Removes blade from the user's inventory.
                user_inv2.remove("blade")

                #Displays the final inventory.
                self.inv_final(user_inv2, inv_points)

        #Displays a death message.
        else:
            
            functions.dead("You should've just used one...")

#Underground (medium) difficulty class.
class Underground(Difficulty):
    
    #Constuctor of the Underground class.
    def __init__(self):
        
        #Inherits from the Difficulty class and sets "Underground" as the difficulty.
        super().__init__("Underground")

    #Part 1 of medium difficulty's gameplay.
    def underground(self, user_inv):
        
        #Stores points based on the value and amount of inventory items the character has.
        inv_points = 0
        
        #The medium situation.
        print("\n\nYou're not in the best situation...but it's also not the worse.")
        print("Although you have to go up an elevator, your escape should be fairly easy.")
        print("Do you decide to wait for a staff member to release you or get out on your own?")
        
        #The user can choose to 'wait' or 'go'.
        #lower() makes the input not case-sensitive.
        wait_or_go = input("\nChoose 'wait' or 'go': ").lower()

        #Executes if the user chose "wait".
        if wait_or_go == "wait": 
            
            #Indicates success and the user can proceed.
            print("\nIt didn't take long before a staff member released you from your cell.")
            print("A couple guards look at you but escape should be possible.")
            print("While running away, you grab a piece of candy.")

            #Adds candy to the inventory.
            user_inv.append("candy")

            #Adds 5 points to total for obtaining candy.
            inv_points += 5

            #Current inventory is transferred to part two's inventory.
            user_inv2 = user_inv

            #Part 2 of the story.
            self.underground_p2(user_inv2, inv_points)

        #Executes if the user chose "go".
        elif wait_or_go == "go":
            
            #Indicates that character escaped the cell without receiving candy.
            print("\nYour character was strong enough to get out of the cell.")
            print("However, you were not given candy because of your actions.")

            #Current inventory is transferred to part two's inventory.
            user_inv2 = user_inv

            #Part 2 of the story.
            self.underground_p2(user_inv2, inv_points)

        #Executes if the user does not choose "wait" or "go".
        else:
            
            functions.dead("\nYour character died at a lost opportunity.")

    #Part 2 of medium difficulty's gameplay.
    def underground_p2(self, user_inv2, inv_points):
        
        #The story continues.
        print("\nRegardless if you got candy or not, you run faster.")
        print("While you run away, you notice a potion and blade.")
        print("You pick both items up.")
        
        #Adds potion and blade to the user's inventory.
        user_inv2.extend(("potion", "blade"))

        #Adds 25 points to total points for obtaining potion and blade.
        inv_points += 25

        #User can choose which item to use for escape.
        #lower() makes the input not case-sensitive.
        item_use = input("\nChoose which item to use in your escape: ").lower()

        #If the user chooses "potion"
        if item_use == "potion":
            
            #Stores a random number from 0 to 100.
            rdm_potion_num = random.randint(0, 100)

            #Indicates RNG (random number generator).
            print(f"\nLet's see how effective the potion is via RNG: {rdm_potion_num}")

            #Subtracts 10 from total points for using potion.
            inv_points -= 10
            
            #If the random potion number is less than 40, the character dies.
            if rdm_potion_num < 40:
                
                functions.dead("Your character died because the potion was too strong.")
            
            #If the random number is greater than or equal to 40, the character escapes.
            else:
                    
                print("The potion strengthed your body!")
                
                #Removes potion from the user's inventory.
                user_inv2.remove("potion")
                
                #Displays the final inventory.
                self.inv_final(user_inv2, inv_points)

        #If the user chooses "blade"
        elif item_use == "blade":
        
            #Stores a random number from 0 to 100.
            rdm_num = random.randint(0, 100)
            
            #Indicates RNG (random number generator).
            print(f"\nLet's see how effective the blade is via RNG: {rdm_num}")

            #Subtracts 15 from total points for using blade.
            inv_points -= 15

            # If the random number is less than 50, the character dies.
            if rdm_num < 50:

                functions.dead("\nYour escape attempt failed and got you killed.")
            
            # If the random number is greater than or equal to 50, the character escapes.
            else:
                
                #Removes blade from the user's inventory.
                user_inv2.remove("blade")
                
                #Displays the final inventory.
                self.inv_final(user_inv2, inv_points)

        #Displays a death message.
        else:
            
            functions.dead("You should've just used one...")
