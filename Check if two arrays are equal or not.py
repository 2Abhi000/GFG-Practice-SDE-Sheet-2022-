#Check if two arrays are equal or not
def rev(aa,bb):
    if len(set(aa).intersection(set(bb)))==len(aa):
        print(1)
    else:
        print(0)
aa=[]
bb=[]
n=int(input("Size: "))
for i in range(n):
    aa.append(int(input("Value: ")))
n2=int(input("Size: "))
for i in range(n2):
    bb.append(int(input("Value: ")))
ans=rev(aa,bb)
