import random
import time
import numpy as np
import sys
import tkinter
from tkinter import *
import WelcomeFinished  # runs the welcome file first


# Fancy Delay Print

def delay_print(s):
    # prints one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


play = True

while play:
    # Create the class Pokimal
    class Pokimal:
        def __init__(self, name, types, moves, EVs, health='==================='):
            # save variables as attributes in the class pokimal
            self.name = name
            self.types = types
            self.moves = moves
            self.attack = EVs['ATTACK']
            self.defense = EVs['DEFENSE']
            self.health = health
            self.bars = 20  # Amount of health bars

        def fight(self, Pokimal2):
            # Allows the pokimals to fight each other

            # Print fight information
            global string_2_attack, string_1_attack
            print("------POKIMAL BATTLES!!!------")
            print(f"\n{self.name}")
            print("TYPE/", self.types)
            print("ATTACK/", self.attack)
            print("DEFENSE/", self.defense)
            print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
            print("\nVS")
            print(f"\n{Pokimal2.name}")
            print("TYPE/", Pokimal2.types)
            print("ATTACK/", Pokimal2.attack)
            print("DEFENSE/", Pokimal2.defense)
            print("LVL/", 3 * (1 + np.mean([Pokimal2.attack, Pokimal2.defense])))

            time.sleep(2)  # Give them a Chance to read

            # Consider type advantages
            version = ['Fire', 'Water', 'Grass']
            for i, k in enumerate(version):  # if the types are the same then the moves will not be very effective
                if self.types == k:
                    # Both are same type
                    if Pokimal2.types == k:
                        string_1_attack = '\nIts not very effective... \n'
                        string_2_attack = '\nIts not very effective... \n'

                    # Pokimal 2 is stronger than Pokimal 1
                    if Pokimal2.types == version[
                        (i + 1) % 3]:  # p1 +1 will always be stronger eg water will be better than fire
                        Pokimal2.attack *= 2  # in the parameter of 3 so it doesnt go to 4
                        Pokimal2.defense *= 2  # doubles p2's attack and defence and halves p1's attack and defense
                        self.attack /= 2
                        self.defense /= 2
                        string_1_attack = '\nIts not very effective... \n'  # p1 attacks are not effective
                        string_2_attack = '\nIts super effective! \n'  # p2 attacks are very affective

                    # Pokimal 2 is weaker than opponent
                    if Pokimal2.types == version[
                        (i + 2) % 3]:  # adds 2 to P1 type will always be weaker eg grass weaker than
                        # fire and fire is weaker than water
                        self.attack *= 2  # doubles p1's attack and defence
                        self.defense *= 2
                        Pokimal2.attack /= 2  # halves p2's attack and defence
                        Pokimal2.defense /= 2
                        string_1_attack = '\nIts super effective! \n'  # p1 moves are very effective
                        string_2_attack = '\nIts not very effective... \n'  # p2 moves are not very effective

            # fighting but making sure they are both alive to continue
            while (self.bars > 0) and (Pokimal2.bars > 0):  # both health is greater than 0
                # Print the health of each pokimal
                print(f"\n{self.name}\t\tHLTH\t{self.health}")
                print(f"{Pokimal2.name}\t\tHLTH\t{Pokimal2.health}\n")

                print(f"Go {self.name}!")  # pokimal 1's turn
                for i, x in enumerate(self.moves):
                    print(f"{i + 1}.", x)  # prints the moves until they are all printed
                while True:
                    try:  # see if its a valid input
                        index = int(input('Pick a move: use 1,2,3 or 4 please! '))
                        if 4 >= index > 0:  # have to answer with 1 2 3 and 4
                            delay_print(
                                f"\n{self.name} used {self.moves[index - 1]}!")  # prints p1 and the move it uses
                            time.sleep(
                                1)  # halts the code so user can read the moves before they are able to input again
                            delay_print(string_1_attack)
                            break
                    except ValueError:
                        print("\nplease enter a valid input")  # tells them to re-input

                # Determine the amount of damage P1 does to P2
                Pokimal2.bars -= self.attack
                Pokimal2.health = ""

                # Add back bars of health
                for j in range(int(Pokimal2.bars + .1 * Pokimal2.defense)):
                    Pokimal2.health += "="

                time.sleep(1)
                print(f"\n{self.name}\t\tHLTH\t{self.health}")  # print P1's health
                print(f"{Pokimal2.name}\t\tHLTH\t{Pokimal2.health}\n")  # prints P2's health
                time.sleep(.5)

                # Check to see if Pokimal 1 has fainted
                if Pokimal2.bars <= 0:
                    delay_print("\n..." + Pokimal2.name + ' fainted. ')
                    delay_print("PLAYER 1 WINS!!!")  # if p2 pokimal faints then p1 won
                    break

                # Pokimal2's turn

                print(f"Go {Pokimal2.name}!")  # print pokimal 2's name
                for i, x in enumerate(Pokimal2.moves):  # prints out the moves until list of moves is complete
                    print(f"{i + 1}.", x)
                while True:  # if you enter any other input except the move number, you have to re input
                    try:
                        index = int(input('Pick a move: use 1,2,3 or 4 please! '))
                        if 4 >= index > 0:
                            delay_print(
                                f"\n{Pokimal2.name} used {Pokimal2.moves[index - 1]}!")  # delay prints pokimal 2 and
                            time.sleep(1)  # its attack
                            delay_print(string_2_attack)
                            break
                    except ValueError:
                        print("\nplease enter a valid input")  # re-input until user inputs 1-4

                # Determine damage p1 takes from p2
                self.bars -= Pokimal2.attack
                self.health = ""

                # Add back bars plus defense boost
                for j in range(int(self.bars + .1 * self.defense)):
                    self.health += "="

                time.sleep(1)
                print(f"{self.name}\t\tHLTH\t{self.health}")  # prints p1 health
                print(f"{Pokimal2.name}\t\tHLTH\t{Pokimal2.health}\n")  # prints p2 health
                time.sleep(.5)

                # Check to see if Pokemon fainted
                if self.bars <= 0:  # if p1 remaining bars/health are 0 or less
                    delay_print("\n..." + self.name + ' fainted. ')
                    delay_print("PLAYER 2 WINS!!!")  # if p1 pokimal faints it says p2 won
                    break


    if __name__ == '__main__':
        # Create Pokemon and all their attributes
        overpowered = Pokimal('Over Powered', 'Fire', ['Alt F4', 'Falcon Punch', 'Flamethrower', 'Machine Gun'],
                              {'ATTACK': 10, 'DEFENSE': 10})
        panik = Pokimal('PANIK!!!', 'Water', ['Scream', 'Shell', 'Cower', 'Whiff'], {'ATTACK': 10, 'DEFENSE': 10})
        onionturtle = Pokimal('Onion Turtle', 'Grass', ['Cry', 'Spice', 'Blind', 'Stinky Breath'],
                              {'ATTACK': 8, 'DEFENSE': 12})

        mascot = Pokimal('Mascot', 'Fire', ['Chant', 'Motivate', 'Dance', 'Support'], {'ATTACK': 4, 'DEFENSE': 2})
        useless = Pokimal('Useless', 'Water', ['Twidling Thumbs', 'Busy', 'Fall Over', 'Disappear'],
                          {'ATTACK': 2, 'DEFENSE': 2})
        punchyrockdude = Pokimal('Punchy Rock Dude', 'Grass', ['Punch', 'Rage', 'Brawl', 'Hurl'],
                                 {'ATTACK': 4, 'DEFENSE': 2})

    pokimals = (overpowered, panik, onionturtle, mascot, useless, punchyrockdude)  # list of pokimals
    randomp1 = random.choice(pokimals)  # chooses a random pokimal for you out of the list
    randomp2 = random.choice(pokimals)  # chooses random opponent out of the list

    if randomp1 == randomp2:  # making it so that the same pokimals don't vs each other eg. mascot vs mascot
        randomp2 = random.choice(pokimals)  # re-rolls random p2 again to get another pokimal until both are different
        randomp1.fight(randomp2)
    else:
        randomp1.fight(randomp2)  # Makes them fight

    # victory screen pops up
    victory = Tk()
    victory.geometry('500x500')
    victory.title("Victory Page")
    victory.configure(bg="light blue")
    victoryspeech = Label(text="VICTORY", font=("Bahnschrift Bold", 50), fg="Yellow", bg="light blue")
    victoryspeech.place(relx=0.5, rely=0.5, anchor=CENTER)  # places the label in the center
    victory.mainloop()  # run the victory screen

    again = str(input("\n Would you like to play again? type yes or no"))
    if again == "no":
        play = False
