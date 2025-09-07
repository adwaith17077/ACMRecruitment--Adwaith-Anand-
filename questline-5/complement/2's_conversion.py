def twoscomplement(x):
    if x<0:
        a=-x
        b=bin(a)
        g=b+bin(1)
        print(format(g,'08b'))

x=-42
twoscomplement(x)
