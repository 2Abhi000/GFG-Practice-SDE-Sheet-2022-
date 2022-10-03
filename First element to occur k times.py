#First element to occur k times
def kele(ar,k):
    are=[]
    d={}
    for i in range(len(ar)):
        d[ar[i]]=ar.count(ar[i])
    for i in d:
        if d[i]==k:
            are.append(i)
    are.sort()
    if are:
        print(are[0])
    else:
        print(0)
            
a=[]
n=int(input("Size: "))
for i in range(n):
    a.append(int(input("Value: ")))
k=int(input("Enter k: "))
ans=kele(a,k)
