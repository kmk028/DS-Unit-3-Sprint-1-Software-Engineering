from random import randint


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        st = self.price / self.weight
        if st < 0.5:
            return 'Not so stealable...'
        elif (st >= 0.5) & (st < 1):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        exp = self.flammability * self.weight
        if exp < 10:
            return '...fizzle.'
        elif (exp >= 10) & (exp < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=randint(1000000, 10000000)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "..it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 & self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
