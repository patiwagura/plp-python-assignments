# Week 4 - OOP Assignment.
# Create a python class named Person, with attributes name, age, gender.
# introduce() method - prints a message to introduce person (name, age, gender).
# 

class Person():

    # constructor - initialize instance-variables.
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # method to introduce person - prints name, age & gender.
    def introduce(self,):
        print("I am ", self.name, " a ", self.gender, " aged ",  self.age ," years ")

# create object of Person.
pato = Person("Patrick", 30, 'male')
pato.introduce()
