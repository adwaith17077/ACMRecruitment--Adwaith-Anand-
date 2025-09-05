#problem no1
i=0
c=0
while i<1000:
    if i%3==0 or i%5==0:
        c+=i
    i=i+1
print(c)


#problem no6
i=0
x=0
y=0
while i<=100:
    x+=i**2
    y+=i
    i=i+1
diff=abs(x-(y**2))
print(diff)
    
