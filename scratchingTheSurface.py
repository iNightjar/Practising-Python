
# Python topics codes and examples
# datatypes, DataStructures, Functions, operators, Strings

# identity operators | membership operators
from __future__ import division
fruits = ["grapes","barries"]
my_fruits = ["grapes","barries"]
fav_fruits = my_fruits
print(fav_fruits is my_fruits)
print(fav_fruits is not my_fruits)
print("bannanes" in fruits)
print("grapes" in fruits)

# binary operators
print(5&10)
print(5|4)
print(5^4)
print(~7)
print(3<<2)
print(3>>1)

# operator precedence
print(3*2+2-1)
print(5*3 //2) #mulitipication then the flow division

# python strings datatypes
print("hello world")
print("hello world"[1])

# python casting for datatypes
# int()
# float()
# str()
x = 'hello/world'
print(x)
e=9 ; f= 8.5
print(str(e), "and", str(f), " are strings")

# python string methods
g= "hello world"
print(len(g)) # string length() method
print(g.index("world")) # index() method
print(g.capitalize()) # capitalize method
# upper method, # lower method too
# isupper|islower returens boolean experssion
# count method, find method, split method


#build-in functions, functions and methods in python
b = "hello world"
print(len(b))
print(b.upper()) # function