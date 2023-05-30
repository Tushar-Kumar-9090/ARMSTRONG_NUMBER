
## WAP to print 1st 10th armstrong number???

n=1
c=0
while True:
    num=n
    sum=0
    l=len(str(n))
    while num>0:
        rem=num%10
        sum=sum+rem**l
        num=num//10
    if sum==n:
        print(n)
        c+=1
    if c==10:
        break
    n+=1
