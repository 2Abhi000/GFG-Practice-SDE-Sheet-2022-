#Find All Four Sum Numbers
k=[]
def mapt(arr, index, subarr,su): 
    if index == len(arr):
        if len(subarr) != 0:
            if len(subarr)==4 and sum(subarr)==su:
                k.append(subarr)            
    else:
        mapt(arr, index + 1, subarr,su)
        mapt(arr, index + 1, subarr+[arr[index]],su)
n=int(input())
a=[]
for i in range(n):
    a.append(int(input("Enter the value: ")))
su=int(input("Sum: "))
ans=mapt(a,0,[],su)
pp=[]
t=0
for i in k:
    if i not in pp:
        pp.append(i)
    else:
        t=1

for i in pp:
    print(i,end='')
