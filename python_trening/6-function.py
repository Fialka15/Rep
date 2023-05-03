def add(x,y):
    return x+y

print(add(1,2))

print(add('I a', 'm taster'))

def add(a=(1,2,3,4)):
    return a[1]

print(add())

def S(r, pi=3.14159):
    return pi*r**2

print ("S=", S(6))

