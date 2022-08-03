from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError

class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if animal.type == "dog":
            self.dogs.enqueue(animal)

        elif animal.type == "cat":
            self.cats.enqueue(animal)

        else:
            raise InvalidOperationError("Method only accepts cat or dog objects.")

    def dequeue(self, pref):
        if pref == "dog":
            return self.dogs.dequeue()

        if pref == "cat":
            return self.cats.dequeue()

        else:
            return None

class Dog:
    def __init__(self):
        self.type = "dog"

class Cat:
    def __init__(self):
        self.type = "cat"
