l=[]
n=int(input())
for i in range(n):
    ele=input()
    l.append(ele)     
print(l)   
e=[]  
for i in l:
    e.extend(ord(j) for j in i )
print(e)   