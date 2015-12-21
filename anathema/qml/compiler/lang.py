class PropertyDeclaration(object):
	def __init__(self, type, name, value = None):
		self.type = type
		self.name = name
		self.value = value

class ComponentDeclaration(object):
	def __init__(self, basetype, scope):
		self.basetype = basetype
		self.scope = scope
