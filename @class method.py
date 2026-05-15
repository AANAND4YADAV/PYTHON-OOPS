class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        return f"{self.name}says woof!"

class Book:
    total_books=0
    def __init__(self,title):
        self.title=title
        Book.total_books+=1
    @classmethod
    def get_total_count(cls):
        return f"Total books created:{cls.total_books}"
    @staticmethod
    def static_method(x,y):
        return x+y
#creating objects
book1=Book("PYTHON 101")
book2=Book("Clean code")
dog1=Dog("tommy")
print(dog1.bark())
print(Book.get_total_count())
print(Book.static_method(5,3))
