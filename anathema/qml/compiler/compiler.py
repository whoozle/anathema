import grammar

class Compiler(object):
	def __init__(self):
		pass

	def compile(self, data, fname):
		parser = grammar.qmlParser()
		ast = parser.parse(data, 'component_declaration', filename = fname, trace = True)
		print ast
