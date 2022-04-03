from calendar import c
s1="hanshtso"
s2="santhosh"
l=[]
m=[]
if(len(s1)==len(s2)):
    for i in range(len(s1)):
        l.append(ord(s1[i]))
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]>l[j]):
                t=l[i]
                l[i]=l[j]
                l[j]=t  
    for i in range(len(l)):
        k=chr(l[i])       
        print(k,end=" ")  
    print()    
    for i in range(len(s2)):
        m.append(ord(s2[i]))
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            if(m[i]>m[j]):
                z=m[i]
                m[i]=m[j]
                m[j]=z  
    for i in range(len(m)):
        q=chr(m[i])       
        print(q,end=" ")       
    if(k==q):
        print(s1+" and "+ s2 +" are anagram") 
    else:
        print(s1 +" and "+s2+" are not anagrams")
else:
    print(s1+" and "+s2+" are not anagrams")        
                                    