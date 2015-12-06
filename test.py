#!/usr/bin/env python

from anathema import Renderer, Rect, Color

def main(renderer):
	size = renderer.size
	renderer.clear(Color.red)
	renderer.flip()
	while True:
		pass

Renderer(main)
