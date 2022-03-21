n=input().lower()
m=input().lower()
n=n.replace(" ","")
m=m.replace(" ","")
print(n,m,end=" ") 
for i in n:
    for j in m:
        if(i==j):
            n=n.replace(i,"",1)
            m=m.replace(i,"",1)
            break
print(n,m,end=" ")
print()        
count=len(n+m)      
print(count)
if count>0:
    l=["Friends","Lovers","affectionate","marriage","Enemies","Sister"]
    while len(l)>1:
        c=count%len(l)
        index=c-1
        if index>=0:
            k=l[:index]
            r=l[index+1:]
            l=r+k
        else:
            l=l[:len(l)-1]
    print("relationship is:",l[0])  
else:
    print("enter different names")              

