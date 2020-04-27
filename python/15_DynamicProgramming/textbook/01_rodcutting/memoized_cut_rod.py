#python3


# example of time-memory tradeoff
def memoized_cut_rod(p, n):
	r = [-1] * (n+1)
	return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
	if r[n] >= 0:
		return r[n]
	if n == 0:
		q = 0
	else:
		q = -1
		for i in range(1, n+1):
			q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
	r[n] = q
	return q


# p[i] := price of i-inch cut
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
MAX = 4
print( memoized_cut_rod(prices, MAX) )
