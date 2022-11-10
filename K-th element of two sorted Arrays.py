#K-th element of two sorted Arrays
def kth(arr,brr,k):
    c=arr+brr
    c.sort()
    print(c[k-1])
n=int(input("Size: "))
m=int(input("Size: "))
k=int(input("K : "))
a=[]
b=[]
for i in range(n):
    a.append(int(input("Value: ")))
for j in range(m):
    b.append(int(input("Value: ")))
ans=kth(a,b,k)
