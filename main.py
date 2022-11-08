import numpy as np
import time # For time delay
import random # For random number generation


class Pokemon:
    def __init__(self, HP=0, EA="", attribute="", species="", PA="", maxHP=""):
        self.HP = HP
        self.maxHP = maxHP
        self.attribute = attribute
        self.species = species
        self.name = species
        self.EA = EA
        self.PA = PA

    def set_name(self):
        self.name = input("Enter the name of the pokemon: ")
        return self.name


# Pokemon information setting
Unit_info = {"Charmander": {"species": "Charmander", "HP": 50, "EA": "Ember", "attribute": "fire", "PA": "Tackle"},
             "Squirtle": {"species": "Squirtle", "HP": 50, "EA": "Water Gun", "attribute": "water", "PA": "Tackle"},
             "Bulbasaur": {"species": "Bulbasaur", "HP": 50, "EA": "Vine Whip", "attribute": "grass", "PA": "Tackle"}
             }
# Attack damage setting
EA_damage = {"Ember": 10, "Water Gun": 10, "Vine Whip": 10}
PA_damage = {"Tackle": 9}

# Create an instance of Pokémons in dictionary
Charmander = Pokemon(Unit_info["Charmander"]["HP"], Unit_info["Charmander"]["EA"], Unit_info["Charmander"]["attribute"], Unit_info["Charmander"]["species"], Unit_info["Charmander"]["PA"], Unit_info["Charmander"]["HP"])
Squirtle = Pokemon(Unit_info["Squirtle"]["HP"], Unit_info["Squirtle"]["EA"], Unit_info["Squirtle"]["attribute"], Unit_info["Squirtle"]["species"], Unit_info["Squirtle"]["PA"], Unit_info["Squirtle"]["HP"])
Bulbasaur = Pokemon(Unit_info["Bulbasaur"]["HP"], Unit_info["Bulbasaur"]["EA"], Unit_info["Bulbasaur"]["attribute"], Unit_info["Bulbasaur"]["species"], Unit_info["Bulbasaur"]["PA"], Unit_info["Bulbasaur"]["HP"])


class Trainer: 
    def __init__(self, name="", poke_list=[], step=0):
        self.name = name
        self.poke_list = poke_list
        self.step = step

    # Add the pokemon to poke_list
    def poke_add(self, poke):
        self.poke_list.append(poke)

    # Remove the pokemon from poke_list
    def poke_remove(self, poke):
        self.poke_list.remove(poke)

    # Print the player pokemon list
    def print_poke_list(self):
        print("This is your actual Pokémon team:")
        for i in range(len(self.poke_list)):
            print(i+1, self.poke_list[i].name,"(",self.poke_list[i].HP,"/",self.poke_list[i].maxHP,")")

    # Pokemon starter choice between Charmander, Squirtle, and Bulbasaur
    def starter_choice(self):
        print("Choose your starter pokemon")
        print("1. Charmander")
        print("2. Squirtle")
        print("3. Bulbasaur")
        while True:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                self.poke_add(Charmander)
                self.poke_list[0].set_name()
                break
            elif choice == 2:
                self.poke_add(Squirtle)
                self.poke_list[0].set_name()
                break
            elif choice == 3:
                self.poke_add(Bulbasaur)
                self.poke_list[0].set_name()
                break
            else:
                print("Please enter a valid number")

    # Pokemon chossing Method
    def choose_poke(self):
        print("Choose your Pokémon:")
        self.print_poke_list()
        while True:
            choice = int(input("Enter the number of your choice: "))
            if choice > 0 and choice <= len(self.poke_list):
                self.poke_list[choice-1].set_name()
                return self.poke_list[choice-1]
            else:
                print("Please enter a valid number")

    def steps(self):
        self.step += 1
        return self.step

# Numpy function
def direction():
    matrix = np.array([[0, 0], [0, 0]])
    matrix[0][0] = 1 # North
    matrix[0][1] = 2 # South
    matrix[1][0] = 3 # East
    matrix[1][1] = 0 # West

    # Randomize the matrix
    np.random.shuffle(matrix)

    # Let the player choose the direction bewteen north, south, east, and west
    print("Choose the direction you want to go")
    print("1. North")
    print("2. South")
    print("3. East")
    print("4. West")
    while True:
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            print("You are going north")
            result = matrix[0][0]
            break
        elif choice == 2:
            print("You are going south")
            result = matrix[0][1]
            break
        elif choice == 3:
            print("You are going east")
            result = matrix[1][0]
            break
        elif choice == 4:
            print("You are going west")
            result = matrix[1][1]
            break
        else:
            print("Please enter a valid number")

    # Print the result
    # print("The result is:", result)
    # if result == 1:
    #     print("Charmander")
    # elif result == 2:
    #     print("Squirtle")
    # elif result == 3:
    #     print("Bulbasaur")
    # else:
    #     print("Nothing")

    return result


# Main function
def main():
    # 1. Set the trainer’s name
    trn_name = input("Set the name of your trainer: ")
    trn = Trainer(trn_name)
    print("Your name is:", trn.name)
    # 2. Choose the starter Pokémon among (Charmander, Bulbasaur, Squirtle)
    # 3. Set the name of Pokémon you choose
    trn.starter_choice()
    # Print the pokemon list
    trn.print_poke_list()

    # 4. Trainer’s goal is to become a Pokémon master, to achieve his/her dream, trainer has 3 steps left to Pokémon master.
    trn.steps()
    print("You have", trn.steps() - 3, "step left to become a Pokémon master")
    if(trn.steps() > 3):
        print(trn.name, "became a Pokémon master ! Congratulation !")
        print("The end")
        return 0
    else:
        # 5. Trainer can choose 4 ways to walk, each of east, west, north, south.
        direction()
        if(direction() == 1):
            print("Wild Charmander appeared")
            
        elif(direction() == 2):
            print("Wild Squirtle appeared")

        elif(direction() == 3):
            print("Wild Bulbasaur appeared")

        else:
            print("Lucky you, there is nothing here")


main()