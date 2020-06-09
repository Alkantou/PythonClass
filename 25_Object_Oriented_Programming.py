print(type(1))
print(type([]))
print(type(()))
print(type({}))


# Create a new object type called Sample
class Sample:
    pass


# Instance of Sample
x = Sample()

print(type(x))


class Dog:
    def __init__(self, breed):
        self.breed = breed


sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

print(sam.breed, frank.breed)


# Note how we don't have any parentheses after breed; this is because it is an
# attribute and doesn't take any arguments.

# class object attributes

class Dog:
    # Class Object Attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


sam = Dog('Lab', 'Sam')

print(sam.name, sam.breed, sam.species)


# METHODS

class Circle:
    pi = 3.14

    # Circle gets instantiated with a radius (default is 1)
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle(2)

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())


# INHERITANCE

# Inheritance is a way to form new classes using classes that have already
# been defined. The newly formed classes are called derived classes, the
# classes that we derive from are called base classes.

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


d = Dog()
print(d)
print(d.eat())
print(d.whoAmI())
print(d.bark())


# POLYMORPHISM

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Meow!'


niko = Dog('Niko')
felix = Cat('Felix')

print(niko.speak())
print(felix.speak())
#
for pet in [niko, felix]:
    print(pet.speak())


#
def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


#

class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def speak(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):

    def speak(self):
        return self.name + ' says Woof!'


class Cat(Animal):

    def speak(self):
        return self.name + ' says Meow!'


fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())


# SPECIAL METHODS


class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("Python Rocks!", "Jose Portilla", 159)

# Special Methods
print(book)
print(len(book))
del book
