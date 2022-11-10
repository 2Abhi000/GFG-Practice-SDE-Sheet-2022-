
#Sum of Middle Elements of two sorted arrays
def su(arr,brr):
    c=arr+brr
    c.sort()
    l=0
    high=len(c)
    mid=l+high/2
    print(c[int(mid)]+c[int(mid-1)])

n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(int(input("Enter the value: ")))

for i in range(n):
    b.append(int(input("Enter the value: ")))
    
ans=su(a,b)

