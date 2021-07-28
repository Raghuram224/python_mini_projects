name1=input("Enter your name:").lower()
name2=input("Enter your partner name:").lower()

name1=list(name1)
name2=list(name2)
name3=len(name1+name2)
print(name3)

for i in name1:
    for l in name2:
        if i==l:
            rep1=name1.index(i)
            name1[rep1]="-"
            rep2=name2.index(i)
            name2[rep2]="-"
    
print(name1)
print(name2)
name3=list(name1+name2)
count=0
for i in name3:
    if (i !="-" and i !=""):
        count +=1
print(count)
f=["Friends","Love","Affection","Marriage","Enemy","Sibilings"]
while len(f)>1:
    c=count%len(f)
    s_index=c-1
    if s_index >=0:
        left=f[: s_index]
        right=f[s_index+1 :]
        f=right+left
    else:
        f=f[:len(f)-1]
print("reltionship is",f[0])
        


