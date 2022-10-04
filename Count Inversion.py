#Count Inversion
def cou(arr):
    def issorted(ar):
        flag = 0
        if(all(ar[i] <= ar[i + 1] for i in range(len(ar)-1))):
            flag = 1
        if (flag) :
            return True
        else :
            return False
    if issorted(arr):
        print(0)
        return
    fla = 0
    test_list1 = arr[:]
    test_list1.sort(reverse = True)
    if (test_list1 == arr):
        fla = 1
    if (fla) :
        print (len(test_list1))
    else:
        co=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if a[i]>a[j]:
                    co=co+1
                    break
        print(co+1)
a=[]
n=int(input("Size: "))
for i in range(n):
    a.append(int(input("Value: ")))
ans=cou(a)
