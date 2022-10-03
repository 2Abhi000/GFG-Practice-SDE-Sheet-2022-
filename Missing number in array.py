#Missing number in array
def miss(a):
    for i in range(1,len(a)+1):
        if i not in a:
            print(i)
    
n=int(input("Size: "))
n=n-1
ar=[]
for i in range(n):
    ar.append(int(input("Value: ")))
ans=miss(ar)