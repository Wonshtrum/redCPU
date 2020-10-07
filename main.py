from sys import argv
from utils import Options
from isa.test import ISATEST
from isa.lc3 import ISALC
from cpu.test import CPU65
from cpu.lc3 import CPULC

def cpu_test(options):
    prog = [
        "lia", 14,
        "add", 15,
        "hlt"
    ]
    cpu = CPU65(ISATEST, 8, options)
    cpu.load(prog)
    cpu.run()
    return cpu, prog

def cpu_lc3(options):
    prog = [
        ("ldi", 0, 14),
        ("sti", 0, 200),
        ("lda", 1, 14),
        ("ldi", 2, 15),
        ("str", 0, 2),
        ("ldr", 3, 0),
        ("mv", 0, 1),
        "hlt",
    ]
    prog = [
        ("ldi", 0, 1),
        ("mv", 0, 1),
        ("ldi", 0, 2),
        ("ldi", 1, 3),
        ("jmp", 0),
        "hlt",
    ]
    cpu = CPULC(ISALC, 8, options)
    cpu.load(prog)
    cpu.run()
    return cpu, prog

if __name__ == "__main__":
    options = Options(argv)
    if "test" in argv: cpu_test(options)
    if "lc3" in argv: cpu_lc3(options)
