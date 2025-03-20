# # solution1
# def draw_triangle():
#     t = ""
#     for x in range(0, 5):
#         for y in range(0, x + 1):
#             t = t + "*"
#         t = t + "\n"
#     print(t)
# draw_triangle()
# print("finish drawing triangle1")

# #solution2

# def draw_triangle_sol2():
#     t = ""
#     for x in range(0, 5):
#         t = t + "*"
#         print(t)
# draw_triangle_sol2()
# print("finish drawing triangle2")

# #solution3

def draw_triangle_sol3():
    [print('*' * i) for i in range(1, 6)]

draw_triangle_sol3()
print("finish drawing triangle3")