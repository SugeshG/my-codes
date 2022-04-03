l=[]
n=int(input())
for i in range(n):
    ele=int(input())
    l.append(ele)
for i in range(n):
    j=len(l)-1
    while j>0:
        t=l[j]
        l[j]=l[j-1]
        l[j-1]=t
        j=j-1
        print(l)   