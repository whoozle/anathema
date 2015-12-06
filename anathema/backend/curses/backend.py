import curses

class Backend(object):
	def __init__(self, main):
		self.__main = main
		curses.wrapper(self.__wrapper)

	def __wrapper(self, window):
		self.window = window
		size = window.getmaxyx()
		self.width, self.height = size
		self.size = (size[1], size[0])
		main = self.__main
		main()
