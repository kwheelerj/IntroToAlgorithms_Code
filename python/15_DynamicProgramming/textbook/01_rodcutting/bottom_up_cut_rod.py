#python3


# no recursive calls needed
def bottom_up_cut_rod(p, n):
	r = [0] * (n+1)
	for j in range(1, n+1):
		q = -1
		print("about to enter loop")
		for i in range(1, j+1):
			print(f'\ti = {i}, j={j}')
			print(f"\tmax({q}, p[{i}] + r[{j}-{i}])")
			q = max(q, p[i] + r[j-i])
			print(f"\tq={q}")
		print("out of loop")
		r[j] = q
		print(f'r[{j}] = {q}')
		print(f'r = {r}')
	return r[n]


# p[i] := price of i-inch cut
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(prices)
print( bottom_up_cut_rod(prices, 4) )