def func(x, lst=[]): 
    lst.append(x) 
    return lst 

print(func(1)) 
print(func(2)) 
print(func(3, [])) 
print(func(4))

def secret_fn():
    [print("*" * i) for i in range(1,7)]
secret_fn()