n=int(input("enter a number :"))
s=n
t=0
while(n>0):
    i=n%10
    t=t*10+i
    n=n//10
print(s)
if t==s:
    print("palindrome")    
a=int(input("enter a number:"))
sum=0
while a>0:
    r=a%10
    c=r*r*r
    sum=sum+c
    a=a//10
print(sum)    
if a==sum:
    print("amstrong no") 
else:
    print("not a amstrong no")       
