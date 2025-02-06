# def add(*args):
#     args_var = [n for n in args]
#     print(sum(args_var))


# add(3, 5, 8, 9)

# ####

# def calculate (n, **kwargs):
#     print(kwargs)

# calculate(2, add=2, substract=3)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)