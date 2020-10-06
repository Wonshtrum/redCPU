from isa.test import IS
from cpu.test import CPU65
from cpu.lc3 import CPULC

prog = [
    "lia", 14,
    "add", 15,
    "hlt"
]

cpu = CPU65(IS, 8)
cpu.load(prog)
cpu.run()

cpu = CPULC(IS, 8)
cpu.load(prog)
cpu.run()
