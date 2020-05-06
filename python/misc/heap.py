#python3

class Heap:
	# internally, we will used 1-based index, not 0-based
	def __init__(self):
		self.arr = []

	def parent(self, i):
		return i // 2
	
	def left(self, i):
		return 2 * i
	
	def right (self, i):
		return 2 * i + 1
	
	def max(self):
		return self.arr[0]
	
	def heapify(self, i):
		l = self.left(i)
		r = self.right(i)
		if l <= len(self.arr) and self.arr[l-1] > self.arr[i-1]:
			largest = l
		else:
			largest = i
		
		if r <= len(self.arr) and self.arr[r-1] > self.arr[i-1]:
			largest = r
		if largest != i:
			tmp = self.arr[i-1]
			self.arr[i-1] = self.arr[largest-1]
			self.arr[largest-1] = tmp
			self.heapify(largest)

	def insert(self, value):
		self.arr.append(value)
		newIndex = len(self.arr)
		while newIndex != 1 and self.arr[self.parent(newIndex)-1] < self.arr[newIndex-1]:
			self.heapify(self.parent(newIndex))
			newIndex = self.parent(newIndex)


heap = Heap()

print(heap.arr)
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(6)
print(heap.arr)