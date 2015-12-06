import curses

class Backend(object):
	def __init__(self, main):
		self.__main = main
		curses.wrapper(self.__wrapper)

	def __wrapper(self, window):
		self.window = window
		main = self.__main
		main()
