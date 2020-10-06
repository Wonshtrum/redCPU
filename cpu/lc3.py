from binary import *
from cpu.cpu import CPU
from ram import RAM

class CPULC(CPU):
    def __init__(self, IS, pins):
        super().__init__(IS, pins)

        #REGISTERS
        self.PC = [0]*pins #program pointer
        self.SP = [0]*pins #stack pointer
        self.MA = [0]*pins #memory address
        self.IR = [0]*pins #instruction register
        self.DT = [0]*pins #argument register

        self.R = RAM(3, pins)
        self.F = [0]*pins

    def exec(self):
        if self.HLT: return False
        for i in range(8):
            print(self.IR)
            sig = self.IS.get(int2bin(i, 3)+self.IR)
            PC_in, PC_out, PC_count, MA_in, RAM_in, RAM_out, IR_in, IR_out, DT_in, DT_out, R_in, R_out, X_in, ALU_out, ALU_sub, ALU_carry, BRK, HLT = sig


            if PC_out:  self.bus = self.PC
            if RAM_out: self.bus = self.ram.get(self.MA)
            if IR_out:  self.bus = self.IR
            if DT_out:  self.bus = self.DT
            if R_out:   self.bus = self.R[int2bin(0, pins)]

            if ALU_out:
                self.bus = add(self.RA, self.bus, ALU_carry)

            if PC_in:  self.PC = self.bus
            if MA_in:  self.MA = self.bus
            if RAM_in: self.ram.set(self.MA, self.bus)
            if IR_in:  self.IR = self.bus
            if DT_in:  self.DT = self.bus
            if R_in:   self.R[int2bin(0, pins)] = self.bus

            if PC_count: self.PC = add1(self.PC)

            print(sig, self.bus)

            if HLT: self.HLT = True; return False
            if BRK: break
        return True

    def load(self, prog):
        for i, instruction in enumerate(prog):
            if type(instruction) == str:
                instruction = self.IS.bits[instruction]
            if type(instruction) == int:
                instruction = int2bin(instruction, self.pins)
            self.ram.set(int2bin(i, self.pins), instruction)
