def to_twos_complement(x, bits=8):
    return format((x & ((1 << bits) - 1)), f'0{bits}b')


binary = to_twos_complement(-42)
print(binary)  
