# Parent Class
class Animal:
    
    # Constructor of Animal class
    # This runs automatically when an object is created
    def __init__(self, name):
        
        # Storing the name inside the object
        self.name = name

    # Method to display animal information
    def info(self):
        
        # Printing the name of the animal
        print("Animal name:", self.name)


# Child Class
# Dog class inherits properties and methods from Animal class
class Dog(Animal):

    # Constructor of Dog class
    # It takes both name and breed
    def __init__(self, name, breed):

        # Calling parent class constructor
        # This initializes self.name
        super().__init__(name)

        # Storing breed inside the object
        self.breed = breed

    # Method specific to Dog class
    def details(self):

        # Printing dog details
        print(self.name, "is a", self.breed)


# Creating an object of Dog class
d = Dog("TOMMY", "LABRADOR")


# Calling inherited method from Animal class
d.info()

# Calling Dog class method
d.details()
