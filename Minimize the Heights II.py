#Minimize the Heights II
def mini_tower(arr,kn):
    for i in range(len(arr)):
        if arr[i]>kn:
            arr[i]=arr[i]-kn
        else:
            arr[i]=arr[i]+kn
    print(arr[-1]-arr[0])
a=[]
n=int(input("Size: "))
for i in range(n):
    a.append(int(input("Value: ")))
k=int(input("Height: "))
ans=mini_tower(a,k)
