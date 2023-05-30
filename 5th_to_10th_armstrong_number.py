
## WAP to print 5th armstrong number to 10th armstrong number???

n=1
c=0
ll=int(input("Enter The Lower Limit: "))
ul=int(input("Enter The Upper Limit: "))
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
        if c>=ll:
            print(n)
    if c==ul:
        break
    n+=1