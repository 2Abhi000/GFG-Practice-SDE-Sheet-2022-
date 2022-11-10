#Sum of primes
n=input()
a=[]
for i in n:
    for j in range(2,int(i),1):
        if int(i)%int(j)!=0:
            a.append(int(i))
        else:
            break
print(sum(a))
