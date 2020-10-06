from utils import *
from ram import RAM
import types


class CPU:
    def __init__(self, ISA, pins):
        self.pins = pins
        self.HLT = False
        self.ISA = ISA
        self.ram = RAM(pins, pins)
        self.bus = [0]*pins
    
    def op(self):
        raise Exception("not implemented")

    def pre(self):
        pass

    def exec(self):
        if self.HLT: return False
        self.pre()
        for i in range(4):
            print(self.IR)
            sig = self.ISA.get(int2bin(i, self.ISA.max_ct)+self.IR[:self.ISA.pins_in])
            BRK, HLT = self.op(sig)
            input()
            if HLT: self.HLT = True; return False
            if BRK: break
        return True

    def load(self, prog):
        raise Exception("not implemented")

    def run(self):
        while self.exec():
            pass
    
    def pick(self, b1, b2):
        for i in range(b1, b2):
            print(self.ram.get(int2bin(i, self.pins)))

    def load(self, prog):
        i = 0
        for instruction in prog:
            i = self.ISA.convert(i, instruction, self.ram)
