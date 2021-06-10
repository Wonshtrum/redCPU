from cpu.cpu import *


class CPU65(CPU):
    def __init__(self, ISA, pins, options = Default):
        super().__init__(ISA, pins, options)

        #REGISTERS
        self.SP = [0]*pins #stack pointer
        self.MA = [0]*pins #memory address
        self.DT = [0]*pins #argument register

        self.RA = [0]*pins
        self.RX = [0]*pins
        self.RY = [0]*pins

    def op(self, sig):
        PC_in, PC_out, PC_count, MA_in, RAM_in, RAM_out, IR_in, IR_out, DT_in, DT_out, A_in, A_out, X_in, X_out, Y_in, Y_out, ALU_out, ALU_sub, ALU_carry, BRK, HLT = sig

        if PC_out:  self.bus = self.PC
        if RAM_out: self.bus = self.RAM.get(self.MA)
        if IR_out:  self.bus = self.IR
        if DT_out:  self.bus = self.DT
        if A_out:   self.bus = self.RA
        if X_out:   self.bus = self.RX
        if Y_out:   self.bus = self.RY

        if ALU_out: self.bus = add(self.RA, self.bus, ALU_carry)

        if PC_in:   self.PC = self.bus
        if MA_in:   self.MA = self.bus
        if RAM_in:  self.RAM.set(self.MA, self.bus)
        if IR_in:   self.IR = self.bus
        if DT_in:   self.DT = self.bus
        if A_in:    self.RA = self.bus
        if X_in:    self.RX = self.bus
        if Y_in:    self.RY = self.bus

        if PC_count: self.PC = add1(self.PC)
        
        if self.options.verbose:
            print("registers:", [bin2int(_) for _ in (self.RA, self.RX, self.RY)])
        return BRK, HLT
