import grammar
import lang

class IRFactory(grammar.qmlSemantics):
	def property_declaration(self, ast):
		return lang.PropertyDeclaration(ast[1], ast[2])


class Compiler(object):
	def __init__(self):
		pass

	def compile(self, data, filename = None, trace = False):
		parser = grammar.qmlParser()
		ir = IRFactory()
		ast = parser.parse(data, 'component_declaration', filename = filename, trace = trace, semantics = ir)
		print ast
		return ""
