#1.Add two numberser
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
sum=a+b
print("sum is:",sum)

#2.Maximum of two numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print(max(a,b))

#3.Factorial of a number
a=int(input("Enter a number:"))
f=1
for i in range(1,a+1):
    f=f*i
print("factorial is:",f)

#4.find the simple interest
p=float(input("Enter principle amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter Time:"))
si=p*r*t/(100)
print("simple interest:",si)
total=p*si
print("total amount after interest:",total)

#5 find compound interest:
