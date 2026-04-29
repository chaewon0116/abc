def add(a,b):
    return a+b

a=int(input("a:"))
b=int(input("b:"))
op=int("op:")
if op =='+': print(add(a,b))
if op =='-': print(a-b)
if op =='*': print(a*b)
if op =='/': print(a/b)