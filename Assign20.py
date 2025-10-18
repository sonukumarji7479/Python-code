"""
# defalt argument
# take something return somthing
def add(a,b): # a,and b is called formal argument
    c=a+b
    return c

x=int(input("Enter first number:"))
y=int(input("Enter secod number:"))

s=add(x,y)
print(s)

# example 2
def add(a,b): # a,and b is called formal argument
    c=a+b
    return c

s=add(3,8)
print(s)

# exampele 3
def add(a,b,c): # a,and b and c is called formal argument
    d=a+b+c
    return d

s=add(3,8,5)
print(s)

# example 4:
def add(a=0,b=0,c=0): # a,and b is called defalt argument
    d=a+b+c
    return d

x=int(input("Enter first number:"))
y=int(input("Enter secod number:"))
z=int(input("Enter third number:"))

s=add(x,y)
print(s)
"""
#-----------------------------------------------------------
# new topic
def f1():
    print("hello sir")
    
x=f1()
print(x) # function no return anything
print(type(x))

#jab bhi koi function kuch return nhi karta hai to wo None return
# karta hai

#-----------------------------------

# positional Argument
# keyword Arguments

# example
def x1(a,b):
    print("a =",a,"b =",b)
    
x1(10,20)

# keyword Arguments
# example
def x1(a,b):
    print("a =",a,"b =",b)
    
x1(b=10,a=20)

#keyword argument and positional argument
#x1(a=10,20) #Eroor
#x1(20,b=20) #correct
#x1(10,a=20) #Error

# write a program to print average of given number
def average(a,b):
    a=(a+b)/2
    return a

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
s=average(x,y)
print(s)


# average number argumets
def average(*t):
    a=sum(t)/len(t)
    return a

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter first number:"))
v=int(input("Enter second number:"))
s=average(x,y,z,v)
print(s)