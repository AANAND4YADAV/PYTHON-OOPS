# 🐍 Python OOP — Learning Journey

A beginner-friendly project where I learn **Object-Oriented Programming in Python** by following a 6-video series. Each commit represents the completion of one video.

---

## 📚 Progress

| Video | Topic | Status |
|-------|-------|--------|
| 1 | Classes, Objects & Methods | ✅ Done |
| 2 | Inheritance | ✅ Done |
| 3 | - | 🔜 Coming soon |
| 4 | - | 🔜 Coming soon |
| 5 | - | 🔜 Coming soon |
| 6 | - | 🔜 Coming soon |

---

## 📁 What's Covered

### Video 1 — Classes, Objects & Methods

- Creating a **class** in Python
- Using `__init__` to initialize object attributes
- Defining and calling **methods**
- Creating an **instance** of a class
- Modifying object attributes via methods

```python
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = 0

    def speak(self):
        print("Hi I am", self.name)
        print("Hi I am", self.age)
```

---

### Video 2 — Inheritance

- Understanding **parent** and **child** classes
- Using `super()` to call the parent class constructor
- **Overriding** methods in a child class
- Extending parent functionality with new attributes and methods
- The concept of **"is-a"** relationships in OOP

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):                          # Method overriding
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def speak(self):                          # Method overriding
        print(f"{self.name} says: Meow!")


dog = Dog("Rex", "Labrador")
cat = Cat("Whiskers")

dog.speak()   # Rex says: Woof!
cat.speak()   # Whiskers says: Meow!
```

---

## 🚀 How to Run

Make sure you have Python installed, then:

```bash
python main.py
```

No external libraries needed — just plain Python!

---

## 🛠️ Requirements

- Python 3.x

---

## 🎯 Goal

Complete all 6 videos and build a strong foundation in OOP concepts like:

- Classes & Objects
- Inheritance
- Encapsulation
- Polymorphism

---

## 📖 Resources

- 🎥 **[Tech With Tim](https://www.youtube.com/@TechWithTim)** — YouTube channel this series is based on. Highly recommended for beginner to intermediate Python tutorials.

---

*This repo is part of my personal learning journey. Committing after every video to track progress and build consistency.*
