# # this code will run only at link below:
# # https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# def turn_right():
#     n = 3
#     for _ in range(n):
#         turn_left()
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()
#