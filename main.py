from sys import argv
from utils import Options
from isa.test import ISATEST
from isa.lc3 import ISALC
from isa.llc import ISALLC
from cpu.test import CPU65
from cpu.lc3 import CPULC

def cpu_test(options):
    prog = [
        "lia", 14,       # mov al, 14
        "add", 15,       # add al, 15
        "hlt"            # hlt
    ]
    cpu = CPU65(ISATEST, 8, options)
    cpu.load(prog)
    cpu.run()
    return cpu, prog

def cpu_lc3(options):
    prog = [
        ("ldi", 0, 16),  # mov r0, 16
        ("sti", 0, 200), # mov [r0], 200
        ("lda", 1, 16),  # mov r1, [16]
        ("ldi", 2, 15),  # mov r2, 15
        ("str", 0, 2),   # mov [r0], r2
        ("ldr", 3, 0),   # mov r3, [r0]
        ("mv", 1, 0),    # mov r1, r0
        "hlt",           # hlt
    ]
    prog1 = [
        ("ldi", 0, 1),   # l0: mov r0, 1
        ("mv", 1, 0),    # mov r1, r0
        ("ldi", 0, 2),   # mov r0, 2
        ("ldi", 1, 3),   # mov r1, 3
        ("jmp", 0),      # jmp l0
        "hlt",           # hlt
    ]
    if "p1" in options.args:
        prog = prog1
    cpu = CPULC(ISALLC, 8, options)
    cpu.load(prog)
    cpu.run()
    return cpu, prog

if __name__ == "__main__":
    options = Options(argv)
    if "test" in argv: cpu_test(options)
    if "lc3" in argv: cpu_lc3(options)
