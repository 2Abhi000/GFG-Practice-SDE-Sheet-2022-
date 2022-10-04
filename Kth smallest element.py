#Kth smallest element
import sys
def count(nums, mid):
    cnt = 0
    for i in range(len(nums)):
        if nums[i] <= mid:
            cnt += 1
    return cnt
 
def kthSmallest(nums, k):
    low = sys.maxsize
    high = -sys.maxsize - 1
    for i in range(len(nums)):
        low = min(low, nums[i])
        high = max(high, nums[i])
    while low < high:
        mid = low + (high - low) // 2
        if count(nums, mid) < k:
            low = mid + 1
        else:
            high = mid
    return low
 
if __name__ == "__main__":
    nums = []
    k = int(input("K: "))
    n=int(input("Size: "))
    for i in range(n):
        nums.append(int(input("Value: ")))
    print(kthSmallest(nums, k))
