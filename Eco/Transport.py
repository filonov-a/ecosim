__author__ = 'aef'


# Транспортная линия
class Transport:
    volume = 1
    velocity = 1
    N = 1

    def __init__(self, n):
        self.name = n
        return

    def getName(self):
        return self.name
