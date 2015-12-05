import anathema
from anathema.backend import Backend

class Renderer(object):
	def __init__(self, main):
		self.backend = Backend(main)

