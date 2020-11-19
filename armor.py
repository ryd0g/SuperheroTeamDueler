import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        blk = random.randint(0, self.max_block)
        return blk

armor = Armor('shield', 15)
print(armor.name)
print(armor.block())