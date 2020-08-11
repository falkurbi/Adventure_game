import time
import random


items = []

# This is to select a random room number which
# you will find the abductor in it.
DangeRoom = random.randint(1, 3)

names = ["Salem", "Fahad", "Reema", "Razan", "Sulaiman", "Hoda"]


# This function to print and put some time between each line.
def pause(ms, sec):
    print(ms)
    time.sleep(sec)


# These are the first lines of the game (intro).
def intro():
    pause("You find your self tied to a chaire "
          "in a place you don't know.", 1)
    pause(f"{random.choice(names)} needs two keys to get out of "
          "the house", 1)


# This function to see if the player will choose to escape or not.
def runAway_or_stay():
    pause("Enter 1 to try cutting the ropes.", 1)
    pause("Enter 2 to stay and wait.", 1)
    pause("What would you like to do ?", 1)
    while True:
        choice = input("(Please enter 1 or 2).\n")
        if choice == '1':
            pause("You are outside that room. Now you need "
                  "to find these keys", 1)
            pause("You find three rooms inside", 1)
            break
        elif choice == '2':
            pause("The abductor cames and took you away.", 1)
            pause("You lost.", 1)
            again()
        else:
            pause("Try again.", 1)


# The players have to choose between these rooms to look for 2 keys
# and they need to not select the wrong room number if they want to win.
def in_house():
    while True:
        room = input("Which room number do you want to try ?\n"
                     "1- Living room\n"
                     "2- Kitchen\n"
                     "3- Diningroom\n")
        if room == str(DangeRoom):
            pause("The abductor is in this room.", 1)
            pause("You lost", 1)
            again()
        elif DangeRoom == 1:
            if room == '2':
                pause("You are in the kitchen and you find one of "
                      "the two keys for the main door.", 1)
                items.append("Fkey")
                break
            elif room == '3':
                pause("You are in the Diningroom room and you find one "
                      "of the two keys for the main door.", 1)
                items.append("Skey")
                break
        elif DangeRoom == 2:
            if room == '1':
                pause("You are in the Living room and you find one of "
                      "the two keys for the main door.", 1)
                items.append("Fkey")
                break
            elif room == '3':
                pause("You are in the Diningroom room and you find one "
                      "of the two keys for the main door.", 1)
                items.append("Skey")
                break
        elif DangeRoom == 3:
            if room == '1':
                pause("You are in the Living room and you find one of "
                      "the two keys for the main door.", 1)
                items.append("Fkey")
                break
            elif room == '2':
                pause("You are in the Kitchen room and you find one "
                      "of the two keys for the main door.", 1)
                items.append("Skey")
                break
        else:
            pause("Please try again.", 1)


# This function is to chick if the player has the two keys with him/her.
def Final_step():
    while True:
        if 'Fkey' in items and 'Skey' in items:
            pause("You went to the main entrance and opened the door.", 1)
            pause("You got out of the house.", 1)
            pause("You won", 1)
            again()
        else:
            in_house()


# This function is to ask the players if they want to play again or not.
def again():
    while True:
        Q = input("Do you want to play again ?\n"
                  "(Enter yes or no)\n").lower()
        if Q == 'yes' or Q == 'y':
            items.clear()
            Game_start()
        elif Q == 'no' or Q == 'n':
            pause("Thank you for playing.", 1)
            exit()
        else:
            pause("Try again please.", 1)

# This function is gathering all functions together.


def Game_start():
    intro()
    runAway_or_stay()
    in_house()
    Final_step()


Game_start()
