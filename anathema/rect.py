class Rect(object):
	__slots__ = ['left', 'top', 'right', 'bottom']

	def __init__(self, *args):
		nargs = len(args)
		if nargs == 1:
			args = args[0]
			nargs = len(args)

		if nargs == 4:
			self.left, self.top, self.right, self.bottom = args
		elif nargs == 2:
			if isinstance(args[0], tuple) and isinstance(args[1], tuple):
				self.left, self.top = args[0]
				self.right, self.bottom = args[1]
				self.right += self.left
				self.bottom += self.right
			else:
				self.left, self.top = 0, 0
				self.right, self.bottom = args
		elif nargs == 0:
			self.left, self.top, self.right, self.bottom = (0, 0, 0, 0)
		else:
			raise Exception("invalid argument combination for rect ctor")

	@property
	def width(self):
		return self.right - self.left

	@property
	def height(self):
		return self.bottom - self.top

	@property
	def pos(self):
		return (self.left, self.top)

	@property
	def size(self):
		return (self.width, self.height)

	def __repr__(self):
		return "(%d, %d, %d, %d)" %(self.left, self.top, self.right, self.bottom)

