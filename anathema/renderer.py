import anathema
from anathema.backend import Backend
from anathema.rect import Rect

class Surface(object):
	def __init__(self):
		self.__rows = []

	def resize(self, size):
		w, h = size

class Renderer(object):
	def __init__(self, main):
		self.__main = main
		self.__ops = []
		Backend(self.__wrapper)

	def __wrapper(self, backend):
		self.backend = backend
		main = self.__main
		main(self)

	@property
	def size(self):
		return self.backend.size

	def clear(self, color, rect = None):
		self.backend.clear(color, rect)

	def flip(self, rect = None):
		self.backend.flip(rect)
