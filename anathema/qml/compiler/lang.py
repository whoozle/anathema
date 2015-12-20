class PropertyDeclaration(object):
	def __init__(self, type, name):
		self.type = type
		self.name = name

class ComponentDeclaration(object):
	def __init__(self, basetype, scope):
		self.basetype = basetype
		self.scope = scope
