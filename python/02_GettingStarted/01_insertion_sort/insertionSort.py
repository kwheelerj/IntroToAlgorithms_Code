#python3

def insertionSort(A):
	for j in range(1,len(A)):
		key = A[j]
		# insert A[j] into the sorted sequence A[1.. j-1]
		i = j-1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key

def revInsertionSort(A):
	for j in range(1,len(A)):
		key = A[j]
		# insert A[j] into the sorted sequence A[1.. j-1]
		i = j-1
		while i >= 0 and A[i] < key:
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key


#  [101011101]	=	1+4+8+16+64+256			=	349
#  [110110101]	=	1+4+16+32+128+256		=	437
# [1100010010]	=	2+16+256+512			=	786
def binaryAdd(A, B, n):
	if len(A) != n or len(B) != n:
		print("error: both must be of size {}", n)
	result = [0] * (n+1)
	index = n - 1
	carryOver = 0
	while index >= 0:
		result[index+1] = (A[index] + B[index] + carryOver) % 2
		carryOver = 1 if (A[index] + B[index] + carryOver) > 1 else  0
		index -= 1
	result[0] = carryOver
	return result




if __name__ == '__main__':
	arr = [4,2,6,3,5,2,8,1]
	print(arr)

	insertionSort(arr)
	print(arr)

	revInsertionSort(arr)
	print(arr)

	res = binaryAdd([1,0,1,0,1,1,1,0,1],[1,1,0,1,1,0,1,0,1],9)
	print(res) # expect [1,0,1,0,1,1,1,0,1]

