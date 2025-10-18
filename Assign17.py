# python sets:
"""Set items are unordered, unchangeable, and do not allow duplicate values."""
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#* Note: Set items are unchangeable, but you can remove items and add new items.


# INTRODUCTION 
# A set is a built-in data type in Python used to store multiple items in a single variable.
# It is unordered, unindexed, and does not allow duplicate values.

# HOW TO CREATE SET
# set unorderd
# examples
myset={"apple","banana","mango"}
print(myset)
fruits = {"apple", "banana", "mango", "cherry"}
print(fruits)
# कभी order ऐसा आ सकता है: {'apple', 'banana', 'cherry', 'mango'}
# कभी ऐसा: {'banana', 'apple', 'mango', 'cherry'}


# FEATURES OF SETS:
#1.Unordered → Elements का कोई fixed order नहीं होता।
#2.Unique → Duplicate values automatically remove हो जाते हैं।
#3.Mutable (Changeable) → आप set में new elements add/remove कर सकते हैं।
#4.Heterogeneous → अलग-अलग data types रख सकते हैं (int, float, string)।
#5.No Indexing/Slicing → List की तरह index से access नहीं कर सकते।


# Duplicates not allowed
# Sets cannot have two items with the same value.
set_1={"apple","banana","apple","lichi"}
print(set_1)

# set items - data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

# Type ()
myset2={"apple", "banana", "cherry"}
print(type(myset2))

# THE set() constructor
myset3=set(("apple", "banana", "cherry"))
print(myset3)

# Access items

# Example 1.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
# Example 2.
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Example 3.
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# ADD METHOD
thisset={"red","green","yellow","pink"}
thisset.add("orange")
print(thisset)

# update() # add multiple value
phoneset={"iphone","vivo","oppo","samsung"}
colorset={"black,white","blue","green"}
phoneset.update(colorset)
print(phoneset)

# add any iterable
fruitsset={"apple","graps","mango"}
addset={"lichi","kiwi","banana"}
fruitsset.update(addset)
print(fruitsset)

# Remove items
thisset={"apple","banana","lichi"}
thisset.remove("banana")
print(thisset)

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# the del keyword
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# loop items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
# join sets

# union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

#Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

x={"a","b","c","d"}
y = (1, 2, 3)
z=x.union(y)
print(z)

#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3=set.intersection(set2)
print(set3)

# Use & to join two sets:
set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)


# Empty set
s = set()       # सही तरीका
print(type(s))  # <class 'set'>

s = {}          # यह dict (dictionary) होगा, set नहीं
print(type(s))  # <class 'dict'>
