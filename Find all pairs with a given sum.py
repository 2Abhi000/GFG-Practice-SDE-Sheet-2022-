#Find all pairs with a given sum
def findSublists(nums,b, target):
    for i in range(len(nums)):
        for j in range(len(b)):
            if nums[i]+b[j]==target:
                print([nums[i],b[j]])
            
    
 
 
if __name__ == '__main__':
    nums = []
    b=[]
    target = int(input("Target: "))
    n=int(input("size: "))
    for i in range(n):
        nums.append(int(input("Enter Value: ")))
    nl=int(input("size: "))
    for i in range(nl):
        b.append(int(input("Enter Value: ")))
    findSublists(nums, b,target)
