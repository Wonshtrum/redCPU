# RedCPU
This is a python library for building and testing CPUs and instruction sets (ISA).
To work, a CPU is supposed to use a program counter (PC) register and a ROM of micro-instructions (generated from the ISA definition), the rest is subject to implementation.

A CPU definition is composed of:
- a CPU initialization function
- a micro-instruction emulation function
- an ISA definition
- a function for converting assembly to binary
