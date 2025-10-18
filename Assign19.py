# ..............function..................#

# how to creat function
# Take Nothing Return nothing
def add():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a+b
    print("sum is:",c)
    
    add()
    
# take something return nothing
def sub(x,y):
    z=x-y
    print("subtraction",z)
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

sub(a,b)
    

    
