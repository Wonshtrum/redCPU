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
RE = 1<<10
RFB = 1<<11
R_in = 1<<12
R_out = 1<<13
A_in = 1<<14
A_out = 1<<15
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
    RAM_out | DT_in | RE | PC_count,
]

OP_R = 1
OP_C = 2
OP_RC = 3
names = ["nop", "ldi", "ldr", "mv" , "str", "sta", "sti", "jmp", "hlt"]#"add", "sub", "cmp", "hlt"]
ops =   [0    , OP_RC, OP_RC, OP_RC, OP_RC, OP_RC, OP_RC, OP_C , 0]

instructions = [
    [
        0,
    ], read+[
        DT_out | R_in,
    ], read+[
        DT_out | MA_in,
        RAM_out | R_in,
    ], [
        R_out | A_in,
        RFB | A_out | R_in,
    ], read+[
        R_out | MA_in,
        RFB | RAM_in | R_out,
    ], read+[
        DT_out | MA_in,
        RAM_in | R_out,
    ], read+[
        R_out | MA_in,
        DT_in | DT_out,
    ], [
        PC_out | MA_in,
        RAM_out | PC_in,
    ], [
        HLT,
    ]
]

ISALC = ISA(4, 2, M)
ISALC.set_rom([], names, instructions, BRK)
for i, instruction in enumerate(base):
    ISALC.names[f"op{i}"] = int2bin(instruction, M)

def convert(self, i, instruction, ram):
    op1 = None
    if type(instruction) == str:
        instruction = (instruction,)
    if type(instruction) == tuple:
        j = 0
        op = instruction[j]
        op_n = ops[names.index(op)]
        op = self.names[op]
        if op_n == 0:
            op += [0]*4
            pass
        if op_n & OP_R:
            j += 1
            op += [0]+int2bin(instruction[j], 3)
        if op_n & OP_C:
            j += 1
            op1 = int2bin(instruction[j], ram.pins_out)
    if type(instruction) == int:
        op = int2bin(instruction, ram.pins_out)

    ram.set(int2bin(i, ram.pins_in), op)
    i += 1
    if op1:
        ram.set(int2bin(i, ram.pins_in), op1)
        i += 1
    return i
ISALC.convert = patch(convert, ISALC)
