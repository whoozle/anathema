import anathema
from anathema.backend import Backend

class Renderer(object):
	def __init__(self, main):
		self.__main = main
		self.backend = Backend(self.__wrapper)

	def __wrapper(self, window):
		self.window = window
		main = self.__main
		main(self)
