player_name1="raghuram"
player_name2=""

name1=list(player_name1.lower())
name2=list(player_name2.lower())

for i in name1:
    if i in name2:
        
        ind=name1.index(i)
        name1[ind]="-"
        ind=name2.index(i)
        name2[ind]="-"
        print("replaced")
print(name1)
print(name2)

names=name1+name2
count=0
for i in names:
    if(i !="-" and i !=""):
        count+=1

print(count)
f=list("FLAMES")
index=0

while len(f)>1:
    for i in range (count):
        index +=1
        if index > len(f):
            index=1
    f.remove(f[index-1])
    index -=1
print(f)


