# Python Tuples

mytuple=("apple","banana","cherry")
print(mytuple)

# Tuple Length
my_tuple=("mango","orange","papaya")
print(len(my_tuple))

# Create tuple with one items
this_tuple=("apple",)
this_tuple1=("apple")
print(type(this_tuple))
print(type(this_tuple1))

# Tuple Items - Data types
tuple1=("apple","mango","orange")
tuple2=(1,2,3,4,5)
tuple3=(True,False,True)

tuple4=("Apple",3,True,3.4J,"male",2.35)
print(tuple4)
print(type(tuple4)) # Type()

#the tuple() constructor
s1=tuple(("apple","mango","kiwi"))
print(s1)
print(type(s1))

# Access Tuple Items
thistuple=("apple","banana","orange")
print(thistuple[0])
print(thistuple[1])
print(thistuple[2])
# Negative Indexing
print(thistuple[-1])
print(thistuple[-2])
print(thistuple[-3])

#range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# check if item exist
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
#python - Update Tuple
#Change Tuple Values
# Once a tuple is created, you cannot change its values. 
# Tuples are unchangeable, or immutable as it also is called.

x=("apple","mango","ornage")
y=list(x)
y[1]="banana"
x=tuple(y)
print(x)

# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# add items
x=("ayush","rohit","ram")
y=list(x)
y.append("lalu")
x=tuple(y)
print(x)

# add tuple to a tuple
t1 = ("apple", "banana", "cherry")
y = ("orange",)
t1=t1+y
print(t1)

# remove items
x1=("iphone","oppo","vivo")
y1=list(x1)
y1.remove("oppo")
x1=tuple(y1)
print(x1)

#del keywords
m1=("apple","mango","orange")
#del m1
print(m1)

# unpaking a Tuple
fruits=("apple","banana","charry")
(a,b,c)=fruits
print(a,b,c)

# Using Asterisk*
name=("ram","sonu","rajni","rajpalyadav","kelliy","jli","li")
(a,b,c,*red)=name
print(a,b,c,red)

#python- loops Tuple
# for loop
x=("iphone","samsung","motorola")
for i in x:
    print(i)
    
#Loop Through the Index Numbers
tuple_x1=("apple","mango","cherry","coconate")
for i in range(len(tuple_x1)):
    print(tuple_x1[i])
    
# Using a While Loop
k1=("asus","hp","dell","infnix","macbook")
i=0
while i<len(k1):
    print(k1[i])
    i=i+1
    
# python- join tuple
p1=("a","b","c")
p2=(1,2,3)
p3=p1+p2
print(p3)

#multiply tuple
tuple_1=(1,2,3)
print(tuple_1*2)

# tuple method
# count() method
j1=(1,2,3,4,5,6,7,7,7,4,4,4,4,4,4,5,5,5,6,6,6,6,6)
x=j1.count(5)
print(x)

# index() methods
l2=(4,5,6,2,87,12,3)
x=l2.index(5)
print(x)

