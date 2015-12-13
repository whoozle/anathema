class Cell(object):
	__slots__ = ['__attr', '__char', 'modified']

	def __init__(self):
		self.__attr = 0
		self.__char = '.'
		self.modified = True

	@property
	def char(self):
		return self.__char

	@char.setter
	def char(self, value):
		self.modified = True
		self.__char = value

	@property
	def attr(self):
		return self.__attr

	@attr.setter
	def attr(self, value):
		self.modified = True
		self.__attr = value


class Row(object):
	def __init__(self, width):
		self.__cols = [Cell() for i in xrange(0, width)]

	def __getitem__(self, idx):
		return self.__cols[idx]

	def paint(self, backend, y):
		x = 0
		for col in self.__cols:
			if col.modified:
				col.modified = False
				backend.move(y, x)
				backend.puts(col.char, col.attr)
			x += 1

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
