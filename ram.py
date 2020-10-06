from utils import *


class RAM:
    def __init__(self, pins_in = 4, pins_out = 8):
        self.pins_in = pins_in
        self.pins_out = pins_out
        self.bits = { tuple(int2bin(_, pins_in)):[0]*pins_out for _ in range(2**pins_in) }

    def get(self, addr):
        return self.bits[tuple(addr)]

    def set(self, addr, value):
        self.bits[tuple(addr)] = value
