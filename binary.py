def int2bin(v, n):
	return list(1 if v & 1<<i else 0 for i in range(n))

def add(v1, v2, carry = 0):
	r = [0]*len(v1)
	for i, (a, b) in enumerate(zip(v1, v2)):
		r[i] = a ^ b ^ carry
		carry = (a & b) | ((a ^ b) & carry)
	return r

def add1(v1):
	return add(v1, [0]*len(v1), 1)
