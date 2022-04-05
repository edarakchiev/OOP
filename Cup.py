class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def get_free_space(self):
        return self.size - self.quantity

    def fill(self, milliliters):
        if self.get_free_space() >= milliliters:
            self.quantity += milliliters

    def status(self):
        return self.get_free_space()



cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
