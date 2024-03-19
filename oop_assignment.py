#Create a Python class named Person.
#The Person class should have the following attributes:
#name: representing the person's name.
#age: representing the person's age.
#gender: representing the person's gender.
#Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
#Create an instance of the Person class and call the introduce method to display the person's information. """

class Person: #class called person
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self): #method that prints the message
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")

# Create an instance of the Person class
person1 = Person("Lilian", 24, "female")

# Call the introduce method to display the person's information
person1.introduce()
