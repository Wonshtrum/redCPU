from cpu.cpu import *


class CPULC(CPU):
    def __init__(self, ISA, pins, options = Default):
        super().__init__(ISA, pins, options)

        #REGISTERS
        self.SP = [0]*pins #stack pointer
        self.MA = [0]*pins #memory address
        self.DT = [0]*pins #argument register
        self.TMP = [0]*pins #temporary register

        self.RA = [0]*3
        self.R = RAM(3, pins)
        self.F = [0]*pins

    def op(self, sig):
        PC_in, PC_out, PC_count, MA_in, RAM_in, RAM_out, IR_in, IR_out, DT_in, DT_out, RE, RFB, R_in, R_out, A_in, A_out, ALU_out, ALU_sub, ALU_carry, BRK, HLT = sig
        MA = self.MA

        if RE:      self.RA  = self.IR[5:]
        if RFB:     self.RA  = self.DT[:3]

        if PC_out:  self.bus = self.PC
        if RAM_out: self.bus = self.RAM.get(self.MA); self.MA = add1(self.MA)
        if IR_out:  self.bus = self.IR
        if DT_out:  self.bus = self.DT
        if R_out:   self.bus = self.R.get(self.RA)
        if A_out:   self.bus = self.TMP

        if ALU_out: self.bus = add(self.RA, self.bus, ALU_carry)

        if PC_in:   self.PC = self.bus
        if MA_in:   self.MA = self.bus
        if RAM_in:  self.RAM.set(self.MA, self.bus)
        if IR_in:   self.IR = self.bus
        if DT_in:   self.DT = self.bus
        if R_in:    self.R.set(self.RA, self.bus)
        if A_in:    self.TMP = self.bus

        if PC_count: self.PC = add1(self.PC)

        if self.options.verbose:
            print("addresses:", self.RA, MA)
            print("registers:", [bin2int(self.R.get(int2bin(_, 3))) for _ in range(8)])

        return BRK, HLT
