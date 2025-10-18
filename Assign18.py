# Dictionary is 
# dict is a class
# dict is a type
# dict is an iterable
# dict is not a sequence
# dict is mutable
# Each element in a dict is a pair of key-object 
# keys in dict be unuque (duplicate key are not allowed)
# no cocept of indexing
# no support of slicing operator
# unsupported canatenation operator , repition operator and inequality operator

thisdic={
    "brand":"iphone",
    "modal": "relme",
    "year": "2023"
}
print(thisdic)

# DICTIONARY ITEMS
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Dictionary Length
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))

#Dictionary Items - Data Types
#String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

#type
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 

# how to create dictiornory
mydict={"name":"sonu","age":21,"city":"patna"}
print(mydict)

my_dict=dict(name="raju",
             age=23,
             city="kolkta",
             contry="india")
print(my_dict)
print(my_dict["name"])

#Dictionary Access with Loop
student = {
    "name": "Sonu",
    "age": 21,
    "city": "Patna"
}
for x in student:
  print(x,":",student[x])
  
# items() functions
student = {
    "name": "Sonu",
    "age": 21,
    "city": "Patna"
}
for y,x in student.items():
  print(y,":",x)

# type valude,key 
student = {
    "name": "Sonu",
    "age": 21,
    "city": "Patna"
}
print(type(student.items()))
print(student.keys())
print(student.values())

# how to add value and update value
student_name={1:"raju",
              2:"ayush",
              3:"aman",
              5:"abhishek"
              }
student_name[6]="monu"
student_name[1]="dhanu"
print(student_name)

#bulit in type
student_name={1:"raju",
              2:"ayush",
              3:"aman",
              5:"abhishek"
              }

print(len(student_name)) #length of keys
print(max(student_name)) # big key
print(min(student_name)) # small key
print(sum(student_name)) # sum of keys
print(sorted(student_name)) # always return keys vlaue in list[]

# iqulity operator
d1 = {"name": "Sonu", "age": 21}
d2 = {"age": 21, "name": "Sonu"}
print(d1 == d2)   # True (order matter nahi karta)

# how to delete 
student_name={1:"raju",
              2:"ayush",
              3:"aman",
              5:"abhishek"
              }
print(student_name.pop(3))
print(student_name.clear)
del student_name[5]
print(student_name)

# dict comprehention
