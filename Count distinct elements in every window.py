#Count distinct elements in every window
k=[]
def maxim_subarr(arr,window):
    t=1
    for i in range(len(arr)):
        for j in range(i+window):
            if(len(arr[i:j])!=0 and len(arr[i:j])==window-1):          
                k.append(len(set(arr[i:j])))
            else:
                t=0

n=int(input("Size: "))
w=int(input("Window: "))
w=w+1
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
ans=maxim_subarr(a,w)
for i in k:
    print(i,end=' ')
    
