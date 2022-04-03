l=[]
n=int(input("enter the no of elements"))
s=len(l)
for i in range (0,n):
    a=int(input())
    l.append(a)
print(l) 
k=int(input("enter the key :")) 
for i in range(0,n):
    for j in range(0,n):
      if(k==l[j]):
          l[0]=l[j]
          l[j]=l[j+1]
          l[0]=l[j-1]
print(l)
          
          

          
        