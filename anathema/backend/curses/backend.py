import curses
from anathema.rect import Rect

class Color(object):
	black	= curses.COLOR_BLACK
	blue	= curses.COLOR_BLUE
	cyan	= curses.COLOR_CYAN
	green	= curses.COLOR_GREEN
	magenta	= curses.COLOR_MAGENTA
	red		= curses.COLOR_RED
	yellow	= curses.COLOR_YELLOW

class Backend(object):
	def __init__(self, main):
		self.__main = main
		curses.wrapper(self.__wrapper)

	def __wrapper(self, window):
		print curses.COLORS
		for bg in xrange(0, 16):
			for fg in xrange(0, 16):
				idx = 1 + ((bg << 4) | fg)
				curses.init_pair(idx, fg, bg)
		self.window = window
		size = window.getmaxyx()
		self.width, self.height = size
		main = self.__main
		main(self)

	@property
	def size(self):
		return (self.width, self.height)

	def clear(self, color, rect):
		self.window.bkgdset(color)
		self.window.bkgd(color)
		if rect is None:
			self.window.clear()
		else:
			raise Exception("NOT IMPLEMENTED")

	def flip(self, rect):
		self.window.refresh()
