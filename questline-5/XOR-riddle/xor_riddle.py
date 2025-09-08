def xorriddle(x,y):
    #to find n if n^x=y 
    n=y^x  #(n^x)^x=n
             #(n^x)^x=y^x
    print('n is equal to',n)


x=23
y=45
xorriddle(x,y)
