class btree:
	""" Binary Tree class for float numbers """
	def __init__(self, data = None, left = None, right = None):
		""" Initialize a tree with a root and two childs nulls """
		self.data = data
		self.left = left
		self.right = right

	def preorder(self, array):
		""" Gets an empty array and return the array with the element of the tree sorted """
		if self.data:
			if self.left:
				self.left.preorder(array)
			else:
				return array.append(self.data)

			if self.right:
				self.right.preorder(array)
		else:
			return array

	def insert(self, data):
		""" Insert data in the tree, greater than root to right, left otherwise. Repeated values are ignored """
		if self.data:
			if data < self.data:
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
