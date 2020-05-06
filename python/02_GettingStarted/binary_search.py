#python3

def binary_search(arr, val):
	print(arr)
	left = 0
	right = len(arr)-1
	while left <= right:
		mid = (left+right) // 2
		print(f'left={left}, right={right}; mid={mid}')
		if arr[mid] > val:
			right = mid-1
		elif arr[mid] < val:
			left = mid+1
		else:
			return mid
	return -1

ret = binary_search([1, 2, 3, 4, 5, 6], 2)
print(ret)
ret = binary_search([1, 2, 3, 4, 5, 6], 3)
print(ret)
ret = binary_search([1, 2, 3, 4, 5, 6], 2.5)
print(ret)
