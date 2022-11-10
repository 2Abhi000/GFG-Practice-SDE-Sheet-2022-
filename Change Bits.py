#Change Bits
k=int(input())
bi=(str(bin(k))[2:])
s=''
for i in bi:
    if(i=='0'):
        s=s+'1'
    else:
        s=s+i
an=int(s,2)
print(an-k,int(s,2))
