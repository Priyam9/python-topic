a=int(input("enter a number"))
rem=0
sum=0
temp=a
while(a>0):
    rem=a%10
    sum=sum*10+rem
    a//=10
if(temp==sum):
    print("palindrome")
else:
    print("not palindrome")
