n=5
l=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1 ):
            l[i][j]="*"  
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")            
    print()            
print()
#0 as diamond 
n=int(input())
l=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1 or j==0 or i==0 or i==n-1 or j==n-1):
            l[i][j]="*"       
for i in range(n):
    for j in range(n):
        print(l[i][j],end=" ")            
    print()                