class Animal:
    def show(self):
        print("woof!")
class Dog(Animal):
    def show(self):
        print("bark bark")#redefining the legacy = method overriding

d=Dog()
d.show()
