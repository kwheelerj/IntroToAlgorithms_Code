#python3

# 2.3-2
# Rewrite the Merge procedure so that it does not use sentinels,
# instead stopping once either array L or R has had all of its
# elements copied back into A and then copying the remainder of
# the array back into A.

import math

def merge(A, p, q, r):
	n = q - p + 1
	m = r - q
	L = [0] * n
	R = [0] * m
	for i in range(n):
		L[i] = A[p+i]
	for j in range(m):
		R[j] = A[q+j+1]

	i = j = 0
	for k in range(p, r+1):
		if i == n:	# exhausted all of L
			for i2 in range (k, r+1):
				A[i2] = R[j]
				j = j+1
			break
		elif j == m:	# exhausted all of R
			for i2 in range (k, r+1):
				A[i2] = L[i]
				i = i+1
			break
		else:
			if L[i] <= R[j]:
				A[k] = L[i]
				i += 1
			else:
				A[k] = R[j]
				j += 1


def mergeSort(A, p, r):
	if p < r:
		q = math.floor((p+r)/2)
		mergeSort(A, p, q)
		mergeSort(A, q+1, r)
		merge(A, p, q, r)


arr = [2, 4, 5, 7, 1, 2, 3, 6]
print(arr)
merge(arr, 0, 3, 7)
print("-" * 10)
print(arr)

print("=" * 15)

arr2 = [5, 2, 4, 7, 1, 3, 2, 6]
print(arr2)
mergeSort(arr2, 0, len(arr2)-1)
print("-" * 10)
print(arr2)
