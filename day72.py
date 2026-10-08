class Animal:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Animal:", self.name)


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show(self):
        super().show()
        print("Breed:", self.breed)


dog = Dog("Tommy", "Labrador")

dog.show()