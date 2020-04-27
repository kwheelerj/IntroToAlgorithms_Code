#python3

# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11, 12
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

NUM = 35

def fib(n):
	if n == 0: return 0
	if n == 1: return 1
	return fib(n-1) + fib(n-2)

for i in range(NUM):
	print(f"fib{i} = {fib(i)}")


def fib_memo(n):
	f_memo = [-1] * (n+1)
	if n == 0: return 0
	if n == 1: return 1 
	f_memo[0] = 0
	f_memo[1] = 1
	return fib_memo_aux(n-1, f_memo) + fib_memo_aux(n-2, f_memo)

def fib_memo_aux(k, arr):
	if arr[k] >= 0: return arr[k]
	else:
		r = fib_memo_aux(k-1, arr) + fib_memo_aux(k-2, arr)
		arr[k] = r
		return r

print("===========")

for i in range(NUM):
	print(f"fib-{i} = {fib_memo(i)}")


print("===========")

def fib_bu(n):
	if n == 0: return 0
	if n == 1: return 1
	fibt = [0] * (n+1)
	fibt[1] = 1
	for i in range(2, n+1):
		fibt[i] = fibt[i-1] + fibt[i-2]
	return fibt[n]

for i in range(NUM):
	print(f"fib({i}) = {fib_bu(i)}")