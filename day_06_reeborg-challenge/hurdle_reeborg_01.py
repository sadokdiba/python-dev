# this code will run only at link below:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def jump_hurdles():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    n = 3
    for _ in range(n):
        turn_left()

n = 6
for _ in range(n):
    jump_hurdles()
