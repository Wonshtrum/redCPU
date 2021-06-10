from utils import *
from ram import RAM


class CPU:
    def __init__(self, ISA, pins, options = Default):
        self.pins = pins
        self.HLT = False
        self.ISA = ISA
        self.RAM = RAM(pins, pins)
        self.bus = [0]*pins
        self.PC = [0]*pins #program counter
        self.IR = [0]*pins #instruction register
        self.options = options
    
    def op(self):
        raise Exception("not implemented")

    def exec(self):
        if self.HLT: return False
        self.pre()

        for i in range(2**self.ISA.max_ct):
            sig = self.ISA.get(int2bin(i, self.ISA.max_ct)+self.IR[:self.ISA.pins_in])
            if self.options.verbose:
                print(self.IR[:self.ISA.pins_in], i, [code for i, code in zip(sig, self.ISA.sigs) if i])

            BRK, HLT = self.op(sig)

            if self.options.verbose:
                print("bus:", self.bus)
                print("PC:", bin2int(self.PC))
            if self.options.interactive:
                cmd = True
                while cmd:
                    cmd = input(">>> ")
                    exec(cmd)

            if HLT: self.HLT = True; return False
            if BRK: break

        return True

    def pre(self):
        if self.options.verbose:
            print("----------------")
        for sig in self.ISA.base:
            self.op(sig)
        if self.options.verbose:
            print("----------------")

    def run(self):
        while self.exec():
            pass
    
    def load(self, prog):
        i = 0
        for instruction in prog:
            i = self.ISA.convert(i, instruction, self.RAM)

    def pick(self, b1, b2):
        for i in range(b1, b2):
            print(self.RAM.get(int2bin(i, self.pins)))
