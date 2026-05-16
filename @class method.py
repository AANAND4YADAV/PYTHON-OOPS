class Dog:
    '''creates a dog object'''
    def __init__(self,name):
        '''Takes dog name'''
        self.name=name
    def bark(self):
        '''Returns a string of dog's name saying woof'''
        return f"{self.name}says woof!"

class Book:
    '''Create a book object, with a total book counter'''
    total_books=0
    def __init__(self,title):
        '''Takesbook  name and increments total_book counter by 1'''
        self.title=title
        Book.total_books+=1
    @classmethod
    def get_total_count(cls):
        '''Returns total book count'''
        return f"Total books created:{cls.total_books}"
    @staticmethod
    def static_method(x,y):
        '''Adds 2 numbers'''
        return x+y
#creating objects
book1=Book("PYTHON 101")
book2=Book("Clean code")
dog1=Dog("tommy")
print(dog1.bark())
print(Book.get_total_count())
print(Book.static_method(5,3))
