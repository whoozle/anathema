import platform

if platform.system() == 'Linux':
	from anathema.backend.curses import Backend
else:
	raise Exception('unhandled linux')
