import random

location = ["Kitchen", "Ballroom", "Conservatory", "Diving Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
weapons = ["Candlestick", "Daggeer", "Lead Pipe", "Revolver", "Rope", "Spanner"]
jewellery = ["brooches", "rings", "necklaces", "earrings", "pendants", "bracelets", "cufflinks"]


class Owner:
    def __init__(self, name, street, town):
        self.name = name
        self.street = street
        self.town = town

    def display_owner(self):
        print("Owner:", self.name, "of", self.street)
        print()


# class Car:
#     def __init__(self, make, model, reg_no, name, street, town):
#         self.make = make
#         self.model = model
#         self.reg_no = reg_no
#         self.registered_keeper = Owner(name, street, town)
#
#     def display_car(self):
#         print("Car: ", self.make, self.model, self.reg_no)
#         self.registered_keeper.display_owner()


class Location:
    def __init__(self, name, street, town):
        self.location = random.choice(location)
        self.weapon = random.choice(weapons)
        self.registered_location = Owner(name, street, town)

    def display_location(self):
        print("Location: ", "In the", self.location, "used this", self.weapon)
        self.registered_location.display_owner()


class Dog:
    def __init__(self, dog_name, breed, name, street, town):
        self.dog_name = dog_name
        self.breed = breed
        self.owner = Owner(name, street, town)

    def display_dog(self):
        print("Dog: ", self.breed, "called", self.dog_name)
        self.owner.display_owner()


class Jewellery:
    def __init__(self, name, street, town):
        self.jewellery = random.choice(jewellery)
        self.owner_jewellery = Owner(name, street, town)

    def display_jewellery(self):
        print("Jewellery: ", self.jewellery)
        self.owner_jewellery.display_owner()

# car1 = Car("Ford", "Capri", "P4LIN", "Michael Palin", "1 Lumberjack Rise", "Forres")
# car1.display_car()
location1 = Location("Larry Cohen", "Victoria Park St", "Steppes")
location1.display_location()
dog1 = Dog("Bullit", "Bulldog", "John Cleese", "1 Sillie Walk", "Steppes")
dog1.display_dog()
jewellery1 = Jewellery("Anne Jacobs", "Victoria Park St", "Steppes")
jewellery1.display_jewellery()