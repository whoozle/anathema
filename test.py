#!/usr/bin/env python

from anathema import Renderer, Rect, Color

def main(renderer):
	size = renderer.size
	#renderer.clear(Color.red << 4)
	import curses
	renderer.backend.window.bkgdset(0, 0x20 << 8)
	renderer.clear(0x20 << 8)
	renderer.backend.window.bkgdset(0, 0x47 << 8)
	renderer.backend.window.addstr(10, 10, 'HAET')
	renderer.flip()
	renderer.backbuffer[1][1].char = 'x'
	renderer.backbuffer[1][3].char = 'x'
	renderer.backbuffer[1][2].char = 'x'
	renderer.flip()
	while True:
		pass

Renderer(main)
