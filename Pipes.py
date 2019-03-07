import random


class Pipes:
    def __init__(self):
        self.xPos = 200
        self.topLength = random.randint(20, 400)
        self.whitespace = 70
        self.bot = self.topLength + self.whitespace
