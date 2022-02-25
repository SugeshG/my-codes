names=["sugesh","mimo","sandy","abishek"]
length=[len(name) for name in names]
names.sort(key =len)
print(names)
print(len(length))
k=len(length)
s=[]
for i in range(0,k+1):
    if length[0]>length[1]:
        high=length[0]
        low=length[1]
    else:
        high=length[1]
        low=length[0]   
for i in range(2,k):
    if length[i]>high:
        high=length[i]  
    elif length[i]<low: 
        low=length[i]    
s.append(length[i])            
print(length[i])
print(high)
print(low)  