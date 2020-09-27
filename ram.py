from binary import *


class RAM:
	def __init__(self, pin_in = 4, pin_out = 8):
		self.bits = { tuple(int2bin(_, pin_in)):[0]*pin_out for _ in range(2**pin_in) }
	def get(self, addr):
		return self.bits[tuple(addr)]
	def set(self, addr, value):
		self.bits[tuple(addr)] = value
