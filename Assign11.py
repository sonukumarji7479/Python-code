mylist=["apple","banana","cherry"]
print(mylist)

l1=["apple","banana","cherry"]
l2=[1,2,2,3,5,7]
l3=[True,False,True]
print(l1,l2,l3,sep="\n")

mylist=list(("sonu","monu","dhanu"))
print(mylist)

list=["abc",2,True,40.5,'male',3.4j,]
print(list)

l5=[]
print(type(l5))

m1=["books","table","notebooks","pencil"]
print(type(m1))
print(len(m1))

# access one by one index
mylist = ["apple", "banana", "graps"]
print(mylist[0])
print(mylist[1])
print(mylist[2])

# access one by one for loop
mylist = ["apple", "banana", "graps"]
for i in range(len(mylist)):
    print("index",i,"=",mylist[i])
    
# how to delect index
mylist = ["apple", "banana", "graps"]
del mylist[0]
print(mylist)

#how to edit list
mylist=["raju","syam","mohan"]
mylist[1]="ram"
print(mylist)

# How to access any number of function of a class
mylist=["raju","syam","mohan"]
mylist.append("gopal")
print(mylist)

# How to add element at given index in the list
mylist=["raju","syam","mohan"]
mylist.insert(1,"sita")
print(mylist)

# behaviar
list=[1,2,3,4,5]
list.insert(10,6)
print(list)

#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)