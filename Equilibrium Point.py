#Equilibrium Point
def equi(arr):
    if len(arr)==1:
        print(arr[0])
    for i in range(1,len(arr)+1):
        if len(arr[:i])!=0 and len(arr[i:])!=0:
            if sum(arr[:i-1])==sum(arr[i:]):
                print(i)
        
n=int(input("Size: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
ans=equi(a)