#Largest subarray with 0 sum
def findSublists(nums, target):
    k={}
    
    for i in range(len(nums)):
        sum_so_far = 0
        for j in range(i, len(nums)):
            sum_so_far += nums[j]
            if sum_so_far == target:
                k[len(nums[i:j+1])]=sum(nums[i:j+1])
    print(max(k))
 
 
if __name__ == '__main__':
    nums = []
    target = int(input("Target: "))
    n=int(input("size: "))
    for i in range(n):
        nums.append(int(input("Enter Value: ")))
    findSublists(nums, target)
