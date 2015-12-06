class Rect(object):
	__slots__ = ['left', 'top', 'right', 'bottom']

	def __init__(self, *args):
		if len(args) == 4:
			self.left, self.top, self.right, self.bottom = args
		elif len(args) == 2:
			if isinstance(args[0], tuple) and isinstance(args[1], tuple):
				self.left, self.top = args[0]
				self.right, self.bottom = args[1]
				self.right += self.left
				self.bottom += self.right
			else:
				self.left, self.top = 0, 0
				self.right, self.bottom = args
		else:
			raise Exception("invalid argument combination for rect ctor")

	def __repr__(self):
		return "(%d, %d, %d, %d)" %(self.left, self.top, self.right, self.bottom)

