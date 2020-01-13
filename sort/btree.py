class btree:
	""" Binary Tree class """
	def __init__(self, data = None):
		''' Initialize a tree with a root and two childs nulls'''
		self.data = data
		self.left = None
		self.right = None

	def sort(self, array):
		''' Gets an empty array and return the array with the element of the tree sorted '''
		if self.data:
			if self.left:
				self.left.sort(array)
			else:
				return array.append(self.data)

			if self.right:
				self.right.sort(array)
		else:
			return array

	def insert(self, data):
		''' Insert element in the tree, based on the inorder insertion'''
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
