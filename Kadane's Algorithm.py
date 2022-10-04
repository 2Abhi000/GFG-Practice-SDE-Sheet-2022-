#Kadane's Algorithm
def max_Subarray_Sum(my_array, array_size): 
    maxTillNow = my_array[0]  
    maxEnding = 0  
    for n in range(0, array_size):  
        maxEnding = maxEnding + my_array[n]  
        if maxEnding < 0:  
            maxEnding = 0  
        elif (maxTillNow < maxEnding):  
            maxTillNow = maxEnding  
    return maxTillNow
my_array = []
n=int(input("Size: "))
for i in range(n):
    my_array.append(int(input("Value: ")))
print(max_Subarray_Sum(my_array, n))
