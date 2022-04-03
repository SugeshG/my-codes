def get_word(get,n):
    if(n>0):
        s=get.split(" ")
    k=len(get)
    m=len(s)
    if(n<=m):
        return (s[n-1])
    return " "
y=input(" enter the sentence: ")
get=y 
a=int(input("enter th value of n:"))
n=a
print(get_word(y,a))
