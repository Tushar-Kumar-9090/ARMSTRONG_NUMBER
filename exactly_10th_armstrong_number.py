
## WAP to print 10th armstrong number???

n=1
c=0
while True:
    num=n
    summ=0
    l=len(str(n))
    while num>0:
        rem=num%10
        summ=summ+rem**l
        num=num//10
    if summ==n:
        c+=1
    if c==10:
        print(n)
        break
    n+=1