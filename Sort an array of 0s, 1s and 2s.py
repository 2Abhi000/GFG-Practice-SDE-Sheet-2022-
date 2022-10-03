#Sort an array of 0s, 1s and 2s
n=int(input("Size: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
a.sort()
print(a)