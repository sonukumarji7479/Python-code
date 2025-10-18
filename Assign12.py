# packing mathod 
a,b,c=1,2,3
l2=[a,b,c]
print(l2)

# unpacking method
l3=["apple","mango","orange"]
a,b,c=l3
print(a,b,c)

# bulit in method
# you can apply them on any iterable
l1=[10,20,30,40,50]
print(max(l1))
print(len(l1))
print(sum(l1))
print(min(l1))
print(sorted(l1))

# Assending order:
l3=[12,42,30,15,35,70,95]
l4=sorted(l3)
print(l4)

# Disending order
l5=[12,42,30,15,35,70,95]
print(sorted(l5,reverse=True))


# LIST METHOD
l6=list()
print(l6)
l6=list((10,20,30))
print(l6)
l6=list("MysirG")
print(l6)
l6=list(range(10))
print(l6)
l6=list([10,20,30])
print(l6)

l6=list()
print(l6)
l6=list((10,20,30))
print(l6)
l6=list("MysirG")
print(l6)
l6=list(range(10))
print(l6)
# 6=list(10,20,30) # error
print(l6)

#Comparision operator on list
l1=[1,2,3]
l2=[5,6,5]
print(l1==l2)
print(l1<l2)

# concatenation operator
l1=[1,2,3]
l2=[5,6,5]
print(l1+l2)
print(l1*l2)

#slicing operater
l1=[1,2,3,4,5,6]
print(l1[0:4:1])
print(l1[3::-1])