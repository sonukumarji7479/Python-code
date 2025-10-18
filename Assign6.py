# Logical operator:
# not
# and
# or

# not operator
# Example
# logical operator must be written lowercase only
# Condition
# not True ------------> False
# not False -----------> True
print("not operator:")
print(not(True))
print(not(False))
print(not("Education")) # very non empty string is true
print(not(5)) # very non very vlaue is True
print(not(0)) 

# and operator
# Conditon
# 1. Ture and Ture ------> Ture
# 2. Ture and Fasle -----> False
# 3. False and ---  -----> false
print("and operator:")
print(5>1 and 3>2)
print(5>3 and 10<5)
print(5>12 and 3<10)
# non bull operands
print("int type operands")
print(3 and 4) 
print(0 and 5)
print(5 and 1)

# or operator
# Conditon
# 1. false and false ------> false
# 2. false and True -----> True
# 3. Ture and ---  -----> True
print("or operator:")
print(5>10 or 3>6)
print(5>3 or 10<5)
print(25>12 or 3<10)
# non bull operands
print("int type operands")
print(5 or 6)
print(0 or 4)
print(0 or 0)
print("Ram" or "shyam")
print("Sita" and "Geeta")



