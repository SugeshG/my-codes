n=int(input())
low=0
high=n-1
l=[[0 for i in range(n)]for j in range(n)]
v=1
for i in range(int(n+1//2)):
    for j in range(low,high+1):
        l[i][j]=v
        v=v+1
    for j in range(low+1,high+1):
        l[j][high]=v
        v=v+1
    for j in range(high-1,low-1,-1):
        l[high][j]=v  
        v=v+1
    for j in range(high-1,low,-1) :
        l[j][i]=v   
        v=v+1  
    low=low+1
    high=high-1    
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")
    print()    



