a=int(input("enter a number"))
temp=0
sum1=0
temp=a
while(temp>0):
    rem=temp%10
    sum1+=rem**3
    temp=temp//10
    if(sum1==a):
        print("is amstrong")
    else:
        print("not amstrong")