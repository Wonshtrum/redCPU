from binary import *
from ram import RAM


class CPU:
    def __init__(self, IS, pins):
        self.pins = pins
        self.HLT = False
        self.IS = IS
        self.ram = RAM(pins, pins)
        self.bus = [0]*pins
    
    def exec(self):
        return Exception("not implemented")

    def load(self, prog):
        return Exception("not implemented")

    def run(self):
        while self.exec():
            pass
    
    def pick(self, b1, b2):
        for i in range(b1, b2):
            print(self.ram.get(int2bin(i, self.pins)))
