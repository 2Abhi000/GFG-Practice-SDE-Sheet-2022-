#Leaders in an array
a=[1,2,3,4,0]
k=[]
p=[]

for i in range(len(a)):
    c=a[i]
    for j in range(i+1,len(a)):
        if(c>a[j]):
            k.append(c)
        else:
            p.append(c)

k=list(set(k))
m=list(set(k)-set(p))
m.append(a[-1])
print(m)