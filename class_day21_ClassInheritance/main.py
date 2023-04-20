class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):  # *Fish inherits Animal class attributes like breathe..
    def __init__(self):
        super().__init__()  # *... with the addition of this line

    def breathe(self):
        super().breathe()  # Inherit breather class from Animal but extend functionality add something to it
        print("do it underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
