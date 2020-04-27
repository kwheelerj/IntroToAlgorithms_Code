#python3


def LCS_Length(X, Y):
	m = len(X)
	n = len(Y)
	b = [['' for x in range(n+1)] for x in range(m+1)]
	c = [[0 for x in range(n+1)] for x in range(m+1)]

	for i in range(1, m+1):
		for j in range(1, n+1):
			if X[i-1] == Y[j-1]:
				c[i][j] = c[i-1][j-1] + 1
				b[i][j] = "\\"
			elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				b[i][j] = "^"
			else:
				c[i][j] = c[i][j-1]
				b[i][j] = "<"
	return c, b


def Print_LCS(b, X, i, j):
	if i == 0 or j == 0:
		return
	if b[i][j] == "\\":
		Print_LCS(b, X, i-1, j-1)
		print(X[i-1])
	elif b[i][j] == "^":
		Print_LCS(b, X, i-1, j)
	else:
		Print_LCS(b, X, i, j-1)



def printTable(table):
	for i in range(len(table)):
		for j in range(len(table[0])):
			print("X" if table[i][j] == "" else table[i][j], end=' | ')
		print("")


def main():
	sequenceX = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
	sequenceY = ['B', 'D', 'C', 'A', 'B', 'A']

	tableC, tableB = LCS_Length(sequenceX, sequenceY)

	printTable(tableC)
	print('-' * 15)
	printTable(tableB)
	print('=' * 20)
	Print_LCS(tableB, sequenceX, len(sequenceX), len(sequenceY))


def test():
	col_count = 3
	row_count = 4
	t = [[0 for x in range(col_count)] for x in range(row_count)]

	for i in range(row_count):
		for j in range(col_count):
			t[i][j] = f"{i},{j}"
	
	printTable(t)


if __name__ == '__main__':
	# test()
	main()
