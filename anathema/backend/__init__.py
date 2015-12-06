import platform

if platform.system() == 'Linux':
	from anathema.backend.curses import Backend, Color
else:
	raise Exception('unhandled linux')
