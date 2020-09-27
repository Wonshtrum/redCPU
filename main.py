from isa.test import *
from cpu.test import *

prog = [
    "lia", 14,
    "add", 15,
    "hlt"
]

cpu = CPU65(IS, 8)
cpu.load(prog)
cpu.run()
