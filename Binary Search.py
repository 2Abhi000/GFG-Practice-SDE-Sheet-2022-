#Binary Search
def binary_search(arr, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		return -1

arr = []
n=int(input("Enter size: "))
for i in range(n):
    arr.append(int(input("Value: ")))
x = int(input("Enter element: "))
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
	print(str(result))
else:
	print(-1)
