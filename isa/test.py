from utils import *
from isa.isa import ISA


PC_in = 1
PC_out = 1<<1
PC_count = 1<<2
MA_in = 1<<3
RAM_in = 1<<4
RAM_out = 1<<5
IR_in = 1<<6
IR_out = 1<<7
DT_in = 1<<8
DT_out = 1<<9
A_in = 1<<10
A_out = 1<<11
X_in = 1<<12
X_out = 1<<13
Y_in = 1<<14
Y_out = 1<<15
ALU_out = 1<<16
ALU_sub = 1<<17
ALU_carry = 1<<18
BRK = 1<<19
HLT = 1<<20
M = 21

base = [
    PC_out | MA_in,
    RAM_out | IR_in | PC_count,
]
read = [
    PC_out | MA_in,
    RAM_out | DT_in | PC_count,
]

names = ["nop", "lda", "ldx", "ldy", "lia", "lix", "liy", "tax", "txa", "tay", "tya", "sta", "stx", "sty", "jmp", "add", "adx", "ady", "hlt"]
instructions = [
    [
        0,
    ], read+[
        DT_out | MA_in,
        RAM_out | A_in,
    ], read+[
        DT_out | MA_in,
        RAM_out | X_in,
    ], read+[
        DT_out | MA_in,
        RAM_out | Y_in,
    ], read+[
        DT_out | A_in,
    ], read+[
        DT_out | X_in,
    ], read+[
        DT_out | Y_in,
    ], [
        A_out | X_in,
    ], [
        X_out | A_in,
    ], [
        A_out | Y_in,
    ], [
        Y_out | A_in,
    ], read+[
        DT_out | MA_in,
        A_out | RAM_in,
    ], read+[
        DT_out | MA_in,
        X_out | RAM_in,
    ], read+[
        DT_out | MA_in,
        Y_out | RAM_in,
    ], read+[
        DT_out | PC_in,
    ], read+[
        DT_out | ALU_out | A_in,
    ], [
        X_out | ALU_out | A_in,
    ], [
        Y_out | ALU_out | A_in,
    ], [
        HLT,
    ]
]

ISATEST = ISA(8, 3, M)
ISATEST.set_rom(base, names, instructions, BRK)
def convert(self, i, instruction, ram):
    if type(instruction) == str:
        instruction = self.names[instruction]
    if type(instruction) == int:
        instruction = int2bin(instruction, ram.pins_out)
    ram.set(int2bin(i, ram.pins_in), instruction)
    return i+1
ISATEST.convert = patch(convert, ISATEST)
