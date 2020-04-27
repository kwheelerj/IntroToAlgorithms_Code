#python3

# r_n := MAX_[1<=i<=n](p_i + r_(n-i))
def cut_rod(p, n):
	print('\t' * (MAX-n), end='')
	print(f"n={n}")
	if n == 0:
		return 0
	q = -1
	print('\t' * (MAX-n), end='')
	print("entering of for loop")
	for i in range(1, n+1):
		print('\t' * (MAX-n), end='')
		print(f'i = {i}')
		print('\t' * (MAX-n), end='')
		print(f"(recursive call next) find max({q},p[{i}] + cut_rod(p, {n}-{i})")
		print('\t' * (MAX-n), end='')
		print(f'p[{i}] = {p[i]}')
		q = max(q, p[i] + cut_rod(p, n-i))
		print('\t' * (MAX-n), end='')
		print(f"max is {q}")
	print('\t' * (MAX-n), end='')
	print("out of for loop")
	return q 





if __name__ == '__main__':
	# p[i] := price of i-inch cut
	prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

	MAX = 4
	print(prices)
	print( cut_rod(prices, MAX) )
