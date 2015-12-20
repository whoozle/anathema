from compiler.compiler import Compiler

import os
import os.path
import sys
import imp

_runtime = os.path.join(os.path.dirname(__file__), 'qml')

def compile(fname):
	with open(fname) as f:
		data = f.read()
		compiler = Compiler()
		return compiler.compile(data, fname)

class _loader(object):
	def __init__(self, path):
		pass

	def load_module(self, fullname):
		mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
		mod.__file__ = "<%s>" % fullname
		mod.__loader__ = self
		path = fullname.split('.')[1:]
		fname = os.path.join(_runtime, '/'.join(path))
		if os.path.isdir(fname):
			mod.__path__ = []
			mod.__package__ = fullname
			return mod
		fname += os.path.extsep + "qml"
		if not os.path.exists(fname):
			raise ImportError("no module named " + fullname)

		code = compile(fname)
		mod.__package__ = fullname.rpartition('.')[0]
		exec(code, mod.__dict__)
		return mod

class _finder(object):
	def find_module(self, fullname, path = None):
		return _loader(path) if fullname == "qml" or fullname.startswith("qml.") else None

sys.meta_path.append(_finder())
