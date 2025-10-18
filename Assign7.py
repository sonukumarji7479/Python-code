# Bitwise operator & | ^ ~ >> <<
# AND ---> &
# OR  -->  |
# XOR -->  ^
# NOT -->  ~ 
# Right shift --->  >>
# Left shift  --->  <<

"""
AND OPERATOR

0 & 0 ---> 0
0 & 1 ---> 0
1 & 0 ---> 0
1 & 1 ---> 1
"""
# Example
print(25&37)

"""
OR OPERATOR
0 | 0 ---> 0
0 | 1 ---> 1
1 | 0 ---> 1
1 & 1 ---> 1
"""
# Example
print(44|72)

"""
OR OPERATOR
0 ^ 0 ---> 0
0 ^ 1 ---> 1
1 ^ 0 ---> 1
1 ^ 1 ---> 0
"""
# Example
print(56^29)

"""
NOT OPERATOR
~ 0 --> 1
~ 1 --> 0
"""
# Example
# 5 = 00000101
# ~5 =11111010
x=~5
print(x)