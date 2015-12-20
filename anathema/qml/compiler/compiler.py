import grammar

class IRFactory(grammar.qmlSemantics):
	def property_declaration(self, ast):
		print "property declaration", ast
		return ast


class Compiler(object):
	def __init__(self):
		pass

	def compile(self, data, filename = None, trace = False):
		parser = grammar.qmlParser()
		ir = IRFactory()
		ast = parser.parse(data, 'component_declaration', filename = filename, trace = trace, semantics = ir)
		print ast
		return ""
