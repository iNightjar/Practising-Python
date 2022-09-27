# object-oriented programming
# creating a class
from cgi import print_directory
from platform import system_alias

## OOP Seciton 11
class instructors:
    companyName= "TECH ACADEMY"
    
    def __init__(self,courseName, duration): # __init__  --> is the initializer
        # (self) parameter is used to aceess the variables and methods
        # that belongs to the class
        self.courseName = courseName
        self.duration = duration

    def printCourseInfo(self):
        print("My Company Name is: ", instructors.companyName)
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
courseInWebsite.courseName= "Linux Machines Decoding"
courseInWebsite.duration= "30 Hours"
courseInWebsite.printCourseInfo()
print(courseInWebsite.courseName)
print(courseInWebsite.duration)
