from utils import *
from ram import RAM

class ISA(RAM):
    def __init__(self, pins_in, max_ct, pins_out, sigs, name="ISA"):
        super().__init__(pins_in+max_ct, pins_out)
        self.name = name
        self.pins_out = pins_out
        self.pins_in = pins_in
        self.max_ct = max_ct
        self.names = {}
        self.sigs = sigs
        self.base = []
        if pins_out != len(sigs):
            raise Warning("ISA rom pins_out doesn't match signal list length")

    def set_rom(self, names, base, instructions, BRK = 0):
        costs = [len(_)+len(base) for _ in instructions]
        print(self.name, costs, sum(costs), sum(costs)/len(costs))

        self.base = [int2bin(instruction, self.pins_out) for instruction in base]
        N = len(instructions)
        for i in range(2**self.pins_in):
            instruction = []
            if i < N:
                instruction = instructions[i]
                self.names[names[i]] = int2bin(i, self.pins_in)
            L = len(instruction)-1
            for j, sub_instruction in enumerate(instruction):
                if j == L: sub_instruction |= BRK
                self.set(int2bin(j, self.max_ct)+int2bin(i, self.pins_in), int2bin(sub_instruction, self.pins_out))
 
    def convert(self, i, instruction, ram):
        raise Exception("not implemented")
