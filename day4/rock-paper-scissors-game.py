import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock Paper Sicssors Game! ")

list_of_choices = [rock,paper,scissors]
computer_choice = random.randint(0,2)
human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))

print(f"Computer chose:\n{list_of_choices[computer_choice]}")

if human_choice  == computer_choice:
    print(f"You chose:\n{list_of_choices[human_choice]}")
    print("Its a tie")

elif human_choice >= 3 or human_choice < 0 :
    print("You typed an invalid number. You lose!")

elif human_choice == 0 and computer_choice == 2:
    print(f"You chose:\n{list_of_choices[human_choice]}")
    print("You win!")
    
elif computer_choice == 0 and human_choice == 2:
    print(f"You chose:\n{list_of_choices[human_choice]}")
    print("You lose!")
    
elif computer_choice > human_choice:
    print(f"You chose:\n{list_of_choices[human_choice]}")
    print("You lose!")
    
elif human_choice > computer_choice:
    print(f"You chose:\n{list_of_choices[human_choice]}")
    print("You win!")
