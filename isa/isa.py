from utils import *
from ram import RAM

class ISA(RAM):
    def __init__(self, pins_in, max_ct, pins_out):
        super().__init__(pins_in+max_ct, pins_out)
        self.pins_out = pins_out
        self.pins_in = pins_in
        self.max_ct = max_ct
        self.names = {}

    def set_rom(self, base, names, instructions, BRK = 0):
        N = len(instructions)
        for i in range(2**self.pins_in):
            instruction = base
            if i < N:
                instruction = base+instructions[i]
                self.names[names[i]] = int2bin(i, self.pins_in)
            L = len(instruction)-1
            for j, sub_instruction in enumerate(instruction):
                if j == L: sub_instruction |= BRK
                self.set(int2bin(j, self.max_ct)+int2bin(i, self.pins_in), int2bin(sub_instruction, self.pins_out))
                
    def convert(self, i, instruction, ram):
        raise Exception("not implemented")
