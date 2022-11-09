import numpy as np
import time # For time delay
import random # For random number generation


class Pokemon:
    def __init__(self, HP=0, EA="", attribute="", species="", PA="", maxHP=0):
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
Unit_info = {"Charmander": {"species": "Charmander", "HP": 50, "EA": "Ember", "attribute": "fire", "PA": "Tackle", "maxHP": 50},
             "Squirtle": {"species": "Squirtle", "HP": 50, "EA": "Water Gun", "attribute": "water", "PA": "Tackle", "maxHP": 50},
             "Bulbasaur": {"species": "Bulbasaur", "HP": 50, "EA": "Vine Whip", "attribute": "grass", "PA": "Tackle", "maxHP": 50},
             }
# Attack damage setting
EA_damage = {"Ember": 10, "Water Gun": 10, "Vine Whip": 10}
PA_damage = {"Tackle": 9}

# Create an instance of Pokémons in dictionary
Charmander = Pokemon(Unit_info["Charmander"]["HP"], Unit_info["Charmander"]["EA"], Unit_info["Charmander"]["attribute"], Unit_info["Charmander"]["species"], Unit_info["Charmander"]["PA"], Unit_info["Charmander"]["maxHP"])
Squirtle = Pokemon(Unit_info["Squirtle"]["HP"], Unit_info["Squirtle"]["EA"], Unit_info["Squirtle"]["attribute"], Unit_info["Squirtle"]["species"], Unit_info["Squirtle"]["PA"], Unit_info["Squirtle"]["maxHP"])
Bulbasaur = Pokemon(Unit_info["Bulbasaur"]["HP"], Unit_info["Bulbasaur"]["EA"], Unit_info["Bulbasaur"]["attribute"], Unit_info["Bulbasaur"]["species"], Unit_info["Bulbasaur"]["PA"], Unit_info["Bulbasaur"]["maxHP"])


class Trainer: 
    def __init__(self, name="", poke_list=[]):
        self.name = name
        self.poke_list = poke_list

    # Add the pokemon to poke_list
    def poke_add(self, poke):
        self.poke_list.append(poke)

    # Remove the pokemon from poke_list
    def poke_remove(self, poke):
        self.poke_list.remove(poke)

    # Print the player pokemon list
    def print_poke_list(self):
        print("\n\nThis is your actual Pokémon team:")
        for i in range(len(self.poke_list)):
            print(i+1, self.poke_list[i].name,"(",self.poke_list[i].HP,"/",self.poke_list[i].maxHP,")")

    # Pokemon starter choice between Charmander, Squirtle, and Bulbasaur
    def starter_choice(self):
        print("\n\nChoose your starter pokemon")
        print("1. Charmander ", "2. Squirtle ", "3. Bulbasaur\n")
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



def battle_disp(my = Pokemon(),enemy = Pokemon()):
    print("\n######################")
    print("1. Enemy:", enemy.name, "(", enemy.HP, "/", enemy.maxHP, ")")
    print("2. My:", my.name, "(", my.HP, "/", my.maxHP, ")")
    print("######################\n")


def poke_EA(attack=Pokemon(), defend=Pokemon()):
    time.sleep(0.5)
    print(attack.name, "used ", attack.EA, "!")
    if attack.attribute == "fire" and defend.attribute == "grass":
        print("It's super effective!")
        defend.HP -= EA_damage[attack.EA] * 2
    elif attack.attribute == "water" and defend.attribute == "fire":
        print("It's super effective!")
        defend.HP -= EA_damage[attack.EA] * 2
    elif attack.attribute == "grass" and defend.attribute == "water":
        print("It's super effective!")
        defend.HP -= EA_damage[attack.EA] * 2
    elif attack.attribute == "fire" and defend.attribute == "water":
        print("Not very effective")
        defend.HP -= EA_damage[attack.EA] * 0.5
    elif attack.attribute == "water" and defend.attribute == "grass":
        print("Not very effective")
        defend.HP -= EA_damage[attack.EA] * 0.5
    elif attack.attribute == "grass" and defend.attribute == "fire":
        print("Not very effective")
        defend.HP -= EA_damage[attack.EA] * 0.5
    else:
        defend.HP -= EA_damage[attack.EA]


def poke_PA(attack=Pokemon(), defend=Pokemon()):
    time.sleep(0.5)
    print("\n", attack.name, "used", attack.PA, "!")
    defend.HP -= PA_damage[attack.PA]


def poke_cure(poke=Pokemon()):
    poke.HP = poke.maxHP
    print("\n", poke.name, "cured !")


def poke_capture(trn=Trainer(),enemy=Pokemon()):
    if enemy.HP < enemy.maxHP * 0.5:
        if random.random() < 0.9:
            print("gotcha!", enemy.species, "was caught!")
            trn.poke_add(enemy)
            trn.poke_list[-1].set_name()
            trn.poke_list[-1].HP = trn.poke_list[-1].maxHP
            trn.print_poke_list()
            return True
        else:
            print("oh no!", enemy.species, "break free!")
            return False
    else:
        if random.random() < 0.15:
            print("gotcha!", enemy.species, "was caught!")
            enemy.set_name()
            trn.poke_add(enemy)
            poke_cure(enemy)
            trn.print_poke_list()
            return True
        else:
            print("oh no!", enemy.species, "break free!")
            return False


def loading():
    for i in range(3):
        print(".")
        time.sleep(1)


# Numpy function for direction
def direction():
    matrix = np.array([[0, 0], [0, 0]])
    matrix[0][0] = 1 # North
    matrix[0][1] = 2 # South
    matrix[1][0] = 3 # East
    matrix[1][1] = 0 # West

    # Randomize the matrix
    np.random.shuffle(matrix)

    # Let the player choose the direction bewteen north, south, east, and west
    time.sleep(0.5)
    print("Choose the direction you want to go:")
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

    loading()
    return result


# Make function choose_action between 1.Elemental Attack 2.Physical Attack 3.Cure 4.Capture Pokémon 5.Change Pokémon
def choose_action():
    print("Choose the action you want to do:")
    print("1. Elemental Attack")
    print("2. Physical Attack")
    print("3. Cure")
    print("4. Capture Pokémon")
    print("5. Change Pokémon")
    while True:
        choice = int(input("Enter the number of your choice: "))
        if choice == 1:
            return "EA"
        elif choice == 2:
            return "PA"
        elif choice == 3:
            return "cure"
        elif choice == 4:
            return "capture"
        elif choice == 5:
            return "change"
        else:
            print("Please enter a valid number")


# Main function
def main():
    # Welcome
    print("\n\nWelcome to the world of Pokémon!")
    input("\nPress enter to continue")
    # 1. Set the trainer’s name
    trn_name = input("\nSet the name of your trainer: ")
    trn = Trainer(trn_name)
    print("\nGood luck for this adventure", trn.name, "!")
    # 2. Choose the starter Pokémon among (Charmander, Bulbasaur, Squirtle)
    # 3. Set the name of Pokémon you choose
    trn.starter_choice()
    
    trn.print_poke_list()

    # 4. Trainer’s goal is to become a Pokémon master, to achieve his/her dream, trainer has 3 steps left to Pokémon master.
    step = 4
    while step > 1:
        step -= 1
        time.sleep(0.5)
        print("\nYou have", step, "step left to become a Pokémon master\n")
        # 5. Trainer can choose 4 ways to walk, each of east, west, north, south.
        result = direction()
        # 6. Each of the wild Pokémon (Charmander, Bulbasaur, Squirtle, and None) is assigned randomly to each way (no duplicates).
        # B. Otherwise, if the Trainer choose was encountering wild Pokémon, then Pokémon battle starts.
        if(result == 1):
            enemy = Charmander
            print("Wild Charmander appeared")
        elif(result == 2):
            enemy = Bulbasaur
            print("Wild Squirtle appeared")
        elif(result == 3):
            enemy = Squirtle
            print("Wild Bulbasaur appeared")
        else:
            # A. If the path Trainer choose was None, Trainer doesn’t need to fight wild Pokémon but just walk 1 step.
            enemy = None
            print("Lucky you, there is nothing here !")
        
        if (enemy != None):
            battle_disp(trn.poke_list[0], enemy)
            while trn.poke_list[0].HP > 0 and enemy.HP > 0:
                # 8.Every battle starts with the action of the Trainer, Trainer has 5 options below:
                action = choose_action()
                # A. Elemental Attack
                if action == "EA":
                    poke_EA(trn.poke_list[0], enemy)
                # B. Physical Attack
                elif action == "PA":
                    poke_PA(trn.poke_list[0], enemy)
                # C. Cure
                elif action == "cure":
                    poke_cure(trn.poke_list[0])
                # D. Capture wild Pokémon
                elif action == "capture":
                    response = poke_capture(trn, enemy)
                    if response == True:
                        break
                # E. Change Pokémon in my hands
                elif action == "change":
                    trn.poke_change()
                # 10. After each of Pokémon’s turn is over, information of HP left of my Pokémon and wild Pokémon should be printed on python shell
                battle_disp(trn.poke_list[0], enemy)
                if enemy.HP > 0:
                    # 9.After the turn of trainer is finished, wild Pokémon use only elemental attack to attack Trainer’s Pokémon.
                    poke_EA(enemy, trn.poke_list[0])
                    # 10. After each of Pokémon’s turn is over, information of HP left of my Pokémon and wild Pokémon should be printed on python shell
                    battle_disp(trn.poke_list[0], enemy)

            # Heal the enemy Pokémon after the battle
            enemy.HP = enemy.maxHP

    # 11. After trainer complete his/her 3 steps of walking, print the word “{trainer’s name}! Congratulations! You became Pokémon master!”
    print("\n", trn.name, "Congratulations! You became Pokémon master!")
    print("The end ! Thank you for playing !\n")
    return 0


main()