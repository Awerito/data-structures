class btree:
	""" Binary Tree class """
	def __init__(self, data = None):
		# Initialize a tree with a root and two childs nulls
		self.data = data
		self.left = None
		self.right = None

	def printTree(self):
		# Rescript the print method based in the inorder impretion
		if self.data:
			if self.left:
				self.left.printTree()
			print(self.data)
			if self.right:
				self.right.printTree()
		return ""

	def insert(self, data):
		# Insert element in the tree based on the inorder insertion
		if self.data:
			if data <= self.data:
				if self.left:
					self.left.insert(data)
				else:
					self.left = btree(data)
			else:
				if self.right:
					self.right.insert(data)
				else:
					self.right = btree(data)
		else:
			self.data = data
