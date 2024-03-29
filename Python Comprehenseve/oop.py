# object-oriented programming
# creating a class
from cgi import print_directory
from platform import system_alias

# OOP Seciton 11


class instructors:
    companyName = "TECH ACADEMY"

    def __init__(self, courseName, duration):  # __init__  --> is the initializer
        # (self) parameter is used to aceess the variables and methods
        # that belongs to the class
        self.courseName = courseName
        self.duration = duration

    def printCourseInfo(self):
        print("My Company Name is:", instructors.companyName)
        # print("The Course Name: ", instructors.courseName)
        # print("The Course Duration: ", instructors.duration)
        # print("\n")

# a class with no methods

class Pets:
    pass            # build-in


# instantiating object of the class
# elearning = instructors("Becoming a linux developer",7)
# bls = instructors("Django for begineers")
# elearning.printCourseInfo()
 # will print the value of the course attribute
# print(elearning.courseName)
# print(elearning.duration)



# modifying classed, adding attributes
# adding duration attribute to instructors class
courseInWebsite = instructors("Introduction To FreeLancing", "8 Hours")
courseInWebsite.courseName = "Linux Machines Decoding"
courseInWebsite.duration = "30 Hours"
courseInWebsite.printCourseInfo()
print(courseInWebsite.courseName)
print(courseInWebsite.duration)

# Deleting attributes
# del courseInWebsite.duration
# print(courseInWebsite.duration)








# class variables VS instance variables
# Inheritance

class person:
    # constructors of the parent class
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def printName(self):
        print(self.firstName, self.lastName)


florist = person("jane", "flowers")
florist.printName()
# florist.printName() # printInfo() can be called by the child only


class lawyers(person):
    # the child's personal constructors
    def __init__(self, fname, lname, casetype):
        person.__init__(self,fname,lname)
        # self.firstName = fname
        # self.lastName = lname
        self.casetype= casetype


    def printInfo(self):
        print("Hello my name is: ", self.firstName, self.lastName)


happy_lawyers = lawyers("jack", "smiley", "criminal")
# happy_lawyers.printInfo() # function inside the lawyers child
happy_lawyers.printName()
#print(happy_lawyers.casetype)
# printing info after adding the "Hello" sintance
happy_lawyers.printInfo()
print(happy_lawyers.casetype)






# Polymorphism
# the ability of having various forms
print(len("hello")) # len() will print the number ofletters
print(len([20,40,60])) # len() will print number of elements


# polimophic function
def addNumber(a,b,c=1):
    return a + b + c

print(addNumber(8,9)) # will prnt 18
print(addNumber(8,9,4))



# Polymorphism class with methods

class uk():
    def capital_city(self):
        print("london is the capital of uk")

    def langauge(self):
        print("english is the primary languag of uk")


class spain():
    def capital_city(self):
        print("madrid is the capital of spain")

    def langauge(self):
        print("spanish is the primary languag of spain")


def europe(sme7):
    sme7.capital_city()

#instansing
queen = uk()
# # queen.capital_city()

zara = spain()
# # zara.capital_city

europe(queen)
europe(zara)

# for coutry in (queen, zara):
#     coutry.capital_city()
#     coutry.langauge()


# encapsulation
# restricting access to methods and variables to prevent direct data modification

class cars:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
    
    # setter and getter for speed
    def setSpeed(self, value):
        self.__speed = value

    def getSpeed(self):
        return self.__speed
    
    # setter and getter for color
    def setColor(self, value):
        self.__color = value

    def getColor(self):
        return self.__color

ford = cars(250, "green")
nissan = cars(300, "red")
bmw = cars(350, "black")

# ford.speed = 200 # will print error 
# changing a vlaue of a parameter with a setSpeed method, applying encapsulation
ford.setSpeed(46)
print(ford.getSpeed())

# changing the color attribute cant' be done because it's a private attribute
ford.setColor("yellow")
print(ford.getColor())


# abstraction
# using ABC module to provide abtraction
from abc import ABC, abstractclassmethod, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

 # providing implementation by the subclasses 
class square(shape):
    def __init__(self, side):
        self.__side = side
    
   
    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


# myshape = shape()
mysquare = square(5)

# printing the value returned the area and perimeter of the square
print(mysquare.area())
print(mysquare.perimeter())