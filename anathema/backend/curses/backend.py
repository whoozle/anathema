import curses

class Backend(object):
	def __init__(self, main):
		curses.wrapper(main)
