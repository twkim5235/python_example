class Amazon:
    name = None
    strength = 20
    dexterity = 25
    vitality = 20
    energy = 15

    def __init__(self, name = 'Amazon'):
        self.name = name

    def attack(self):
        return 'Jab!!!'
