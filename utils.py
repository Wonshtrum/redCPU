from types import MethodType as patch


class Options:
    @staticmethod
    def valid(arg):
        return len(arg) > 1 and arg[0] == "-" and all(_.isalnum() for _ in arg[1:])

    def __init__(self, args = []):
        self.args = [_[1:] for _ in args if self.valid(_)]
        self.flags = "".join(self.args)
        self.verbose = "v" in self.flags
        self.interactive = "i" in self.flags

Default = Options()

def int2bin(v, n):
    return list(1 if v & 1<<i else 0 for i in range(n))

def bin2int(v):
    return sum(b<<i for i, b in enumerate(v))

def add(v1, v2, carry = 0):
    r = [0]*len(v1)
    for i, (a, b) in enumerate(zip(v1, v2)):
        r[i] = a ^ b ^ carry
        carry = (a & b) | ((a ^ b) & carry)
    return r

def add1(v1):
    return add(v1, [0]*len(v1), 1)
