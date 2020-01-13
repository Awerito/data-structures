import math

class lista:
	def __init__(self, data=None):
		self.data = data
		self.next = None
	
	def newCircle(self):
		if self.data:
			if self.next:
				self.next.newCircle()
			else:
				self.next = lista([0, 0, 0, 0, 0])
		else:
			self.data = [0, 0, 0, 0, 0]
	
	def update(self, data):
		if self.data:
			self.data[0] = data[0]
			self.data[1] = data[1]
			self.data[2] = data[2]
			self.data[3] += data[4]
			# draw circle
			if self.next:
				nx = self.data[0] + self.data[2] * math.cos(self.data[3])
				ny = self.data[1] + self.data[2] * math.sin(self.data[3])
				nr = self.data[2] / 2
				new_data = [nx, ny, nr, self.data[3], data[4]]
				self.next.update(new_data)

	def show(self):
		if self.data:
			print(self.data)
			if self.next:
				self.next.show()
