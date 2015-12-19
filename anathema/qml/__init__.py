from compiler.compiler import Compiler

import os
import os.path

_runtime = os.path.join(os.path.dirname(__file__), 'runtime')

def compile(spec):
	fname = os.path.join(_runtime, spec.replace('.', '/') + os.path.extsep + 'qml')
	with open(fname) as f:
		data = f.read()
		compiler = Compiler()
		return compiler.compile(data, spec)
