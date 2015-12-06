#!/usr/bin/env python

from anathema import Renderer, Rect, Color

def main(renderer):
	size = renderer.size
	#renderer.clear(Color.red << 4)
	import curses
	renderer.backend.window.addstr(10, 10, '?', curses.color_pair(0x79))
	renderer.flip()
	while True:
		pass

Renderer(main)
