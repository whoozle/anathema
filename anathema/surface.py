class Cell(object):
	__slots__ = ['__attr', '__char', '__row', '__x']

	def __init__(self, row, x):
		self.__attr = 0
		self.__char = '.'
		self.__row = row
		self.__x = x

	@property
	def char(self):
		return self.__char

	@char.setter
	def char(self, value):
		self.__char = value
		self.__update()

	@property
	def attr(self):
		return self.__attr

	@attr.setter
	def attr(self, value):
		self.__attr = value
		self.__update()

	def __update(self):
		self.__row.update(self.__x)

class Row(object):
	def __init__(self, width):
		self.__cols = [Cell(self, i) for i in xrange(0, width)]
		self.__invalid = [(0, width)]

	def __getitem__(self, idx):
		return self.__cols[idx]

	def update(self, x):
		pass

	def paint(self, backend, y):
		cols = self.__cols
		for x1, x2 in self.__invalid:
			backend.move(y, x1)
			for x in xrange(x1, x2):
				backend.puts(cols[x].char, cols[x].attr)
		self.__invalid = []

class Surface(object):
	def __init__(self, size):
		self.width, self.height = size
		self.__rows = [Row(self.width) for i in xrange(0, self.height)]

	def resize(self, size):
		raise Exception("implement me")

	def paint(self, backend):
		rows = self.__rows
		for y in xrange(0, len(rows)):
			row = rows[y]
			row.paint(backend, y)

	def __getitem__(self, idx):
		return self.__rows[idx]
