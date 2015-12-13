import anathema
from anathema.backend import Backend
from anathema.rect import Rect
from anathema.surface import Surface

class Renderer(object):
	def __init__(self, main):
		self.__main = main
		self.__ops = []
		Backend(self.__wrapper)

	def __wrapper(self, backend):
		self.backend = backend
		self.backbuffer = Surface(backend.size)
		main = self.__main
		main(self)

	@property
	def size(self):
		return self.backend.size

	def text(self, pos, text, color):
		pass
		#if color is not None:
		#	window.set

	def clear(self, color, rect = None):
		pass

	def flip(self):
		self.backbuffer.paint(self.backend)
		self.backend.flip(0)
