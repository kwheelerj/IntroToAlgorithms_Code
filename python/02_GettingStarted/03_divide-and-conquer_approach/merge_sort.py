#python3

import math

def merge(A, p, q, r):
	n = q - p + 1
	m = r - q
	L = [0] * (n+1)
	R = [0] * (m+1)
	for i in range(n):
		L[i] = A[p+i]
	for j in range(m):
		R[j] = A[q+j+1]

	L[n] = float("inf")
	R[m] = float("inf")

	# return L, R

	i = j = 0
	for k in range(p, r+1):
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
# L,R = merge(arr, 0, 3, 7)
merge(arr, 0, 3, 7)
# print(L)
print("-" * 10)
# print(R)
print(arr)
print("=" * 15)

arr2 = [5, 2, 4, 7, 1, 3, 2, 6]
print(arr2)
mergeSort(arr2, 0, len(arr2)-1)
print("-" * 10)
print(arr2)