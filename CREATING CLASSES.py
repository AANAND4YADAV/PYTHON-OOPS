class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 0
        self.li = [1, 3, 4]

    def speak(self):
        print("Hi I am", self.name)
        print("Hi I am", self.age)

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


aanand = Student("aanand", 19)
aanand.speak()
aanand.change_age(9)
aanand.add_weight(90)
print(aanand.weight)
