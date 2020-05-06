#python3

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None
	
	def insert_left(self, value):
		if self.left_child == None:
			self.left_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.left_child = self.left_child
			self.left_child = new_node

	def insert_right(self, value):
		if self.right_child == None:
			self.right_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.right_child = self.right_child
			self.right_child = new_node

	def dfs_preorder(self):
		print(self.value)
		if self.left_child:
			self.left_child.dfs_preorder()
		if self.right_child:
			self.right_child.dfs_preorder()
	
	def dfs_inorder(self):
		if self.left_child:
			self.left_child.dfs_inorder()
		print(self.value)
		if self.right_child:
			self.right_child.dfs_inorder()

	def dfs_postorder(self):
		if self.left_child:
			self.left_child.dfs_postorder()
		if self.right_child:
			self.right_child.dfs_postorder()
		print(self.value)
	
	def bfs(self):
		queue = []
		queue.append(self)
		
		while len(queue) != 0:
			current_node = queue.pop(0)
			print(current_node.value)
			if current_node.left_child:
				queue.append(current_node.left_child)
			if current_node.right_child:
				queue.append(current_node.right_child)


tree = BinaryTree('a')
tree.insert_left('b')
tree.left_child.insert_right('d')
tree.insert_right('f')
tree.insert_right('c')
tree.right_child.insert_left('e')

##########################################3


tree.dfs_preorder()

print("=" * 15)

tree.dfs_inorder()

print("=" * 15)

tree.dfs_postorder()

print("=" * 15)

tree.bfs()