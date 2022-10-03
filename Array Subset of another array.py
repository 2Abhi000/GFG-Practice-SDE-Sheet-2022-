#Array Subset of another array
def sub(a1,a2):
    if len(set(a1).intersection(set(a2)))==len(a2):
        print("Yes")
    else:
        print("No")
n=int(input("Size: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
m=int(input("Size: "))
b=[]
for i in range(m):
    b.append(int(input("Value: ")))
ans=sub(a,b)