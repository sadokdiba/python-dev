#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as file_with_names:
    names = file_with_names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    whole_letter = starting_letter.read()

for name in names:
    final_letter = whole_letter.replace("[name]", name.strip())
    with open(f"./Output/ReadyToSend/{name.strip()}_Invitation.txt", mode="w") as file:
        file.write(f"{final_letter}")

# disclaimer this code is copyrighted

