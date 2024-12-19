import sys
import time

def type_text(text, typing_speed=0.05):
    """Prints text with a typing effect aligned to the left."""
    for char in text:
        sys.stdout.write(char)  # Print one character at a time
        sys.stdout.flush()  # Flush the buffer to display the character
        time.sleep(typing_speed)  # Pause for a short time between characters
    print()  # Move to the next line after the text is complete

def ascii_art():
    art = r'''
                                                              ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \O/                                      |\
          X.a##a.   M                                       |_\
       .aa########a.>>                                    __|__
    .a################aa.                                 \   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    '''
    print(art)


def shipwreck():
    attempts = 3
    while attempts > 0:
        type_text("You are shipwrecked on the beach of Mystic Island\nWould you like to go \"North\" or \"South\"")
        shipwreck_decision = input().strip().upper()
        if shipwreck_decision == "NORTH":
            type_text("That was close! You find a dense Jungle!\n")
            north()
        elif shipwreck_decision == "SOUTH":
            type_text("You are caught in quicksand. Game Over")
            quit()
        else:
            attempts -= 1
            if attempts == 0:
                type_text("You have exhausted your attempts.")
                game_over()
            type_text(f"Incorrect input. Enter either \"North\" or \"South\" - {attempts} attempts left.")

def north():
    attempts = 3
    while attempts > 0:
        type_text("Now at the Jungle, Climb a tree \"Tree\"? or continue on foot? \"Foot\"")
        north_decision = input().strip().upper()
        if north_decision == "TREE":
            type_text("Almost there! You spot a path leading to a cave!\n")
            climb_a_tree()
        elif north_decision == "FOOT":
            type_text("You are bitten by a snake.")
            game_over()
        else:
            attempts -= 1
            if attempts == 0:
                type_text("You have exhausted your attempts.")
                game_over()
            type_text(f"Incorrect input. Enter either \"Tree\" or or \"Foot\" - {attempts} attempts left.")

def climb_a_tree():
    attempts = 3
    while attempts > 0:
        type_text("Would your like to Enter the cave \"Cave\"? or walk along the river? \"River\"")
        climb_a_tree_decision = input().strip().upper()
        if climb_a_tree_decision == "CAVE":
            type_text("Its getting Scarier! You encounter a sleeping dragon guarding the Crystal!\n")
            sleeping_dragon()
        elif climb_a_tree_decision == "RIVER":
            type_text("You are swept away by the current.")
            game_over()
        else:
            attempts -= 1
            if attempts == 0:
                type_text("You have exhausted your attempts.")
                game_over()
            type_text(f"Incorrect input. Enter either \"Cave\"? or \"River\" - {attempts} attempts left.")

def sleeping_dragon():
    attempts = 3
    while attempts > 0:
        type_text("Now in front of the Dragon! Steal the Crystal \"Steal\"? or befriend the dragon? \"Befriend\"")
        sleeping_dragon_decision = input().strip().upper()
        if sleeping_dragon_decision == "BEFRIEND":
            type_text("Hooray! The dragon gives you the Crystal and flies you off the island.")
            win()
        elif sleeping_dragon_decision == "STEAL":
            type_text("The dragon wakes up and burns you!!!!\n")
            game_over()
        else:
            attempts -= 1
            if attempts == 0:
                type_text("You have exhausted your attempts. Game Over!\nPlease restart and try again.")
                quit()
            type_text(f"Incorrect input. Enter either \"Steal\"? or \"Befriend\" - {attempts} attempts left.")

def game_over():
    type_text("Game over! You can restart the game and try again")
    quit ()
def win():
    type_text("You WIN!!!!!!")
    quit()

def main():
    ascii_art()
    type_text("Welcome to Mystic Island", typing_speed=0.03)
    time.sleep(1)
    type_text("Your mission is to recover the Crystal of Eternity.", typing_speed=0.03)
    time.sleep(1)
    type_text("Good luck!", typing_speed=0.03)
    time.sleep(1)
    shipwreck()
    
if __name__ == "__main__":
    main()
    