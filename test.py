#!/usr/bin/env python

from anathema import Renderer
from anathema.object import aobject

class Foo(aobject):
	pass

foo = Foo()

def onX(value, old):
	print "X: changed to ", value, " from ", old

def onAny(name, value, old):
	print "ANY: changed ", name, " to ", value, " from ", old

foo.on('changed', onAny)
foo.on('changed', 'x', onX)

foo.x = 1
foo.x = 2
foo.x = 3
foo.x = 3

def main(renderer):
	print "hello", renderer
	while True:
		pass

#Renderer(main)
