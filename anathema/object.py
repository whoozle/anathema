import sys
import logging

class aobject(object):
	def __init__(self):
		self.__handlers = {}

	def on(self, event, name, handler):
		h = self.__handlers.setdefault(event, {})
		h = h.setdefault(name, [])
		h.append(handler)

	def emit(self, event, name, *args):
		if name.startswith('_'):
			return

		hs = self.__handlers.get(event, {})
		hs = hs.get(name, [])
		for h in hs:
			try:
				h(*args)
			except Exception as e:
				print sys.exc_info()

	def __setattr__(self, name, value):
		self.emit('set', name, value)
		old = getattr(self, name) if hasattr(self, name) else None
		if value != old:
			self.emit('changed', name, value, old)
		return object.__setattr__(self, name, value)
