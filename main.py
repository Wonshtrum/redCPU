from isa.test import ISATEST
from isa.lc3 import ISALC
from cpu.test import CPU65
from cpu.lc3 import CPULC

"""
prog = [
    "lia", 14,
    "add", 15,
    "hlt"
]
cpu = CPU65(ISATEST, 8)
cpu.load(prog)
cpu.run()
"""

prog = [
    ("ldi", 0, 14),
    "hlt",
]
cpu = CPULC(ISALC, 8)
cpu.load(prog)
cpu.run()
