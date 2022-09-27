# object-oriented programming
# creating a class
from platform import system_alias

## OOP Seciton 11
class instructors:
    companyName= "Linux OpenSource Development"
    
    def __init__(self,course): # __init__  --> is the initializer
        # (self) parameter is used to aceess the variables and methods
        # that belongs to the class
        self.course = course

    def printinfo(self):
        print("My Company Name is: ", instructors.companyName)


# a class with no methods
class Pets:
    pass            # build-in


# instantiating object of the class
elearning = instructors("Becoming a linux developer") 
bls = instructors("Django for begineers")
elearning.printinfo()

print(elearning.course) # will print the value of the course attribute

