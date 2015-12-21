#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS


__version__ = (2015, 12, 21, 18, 57, 29, 0)

__all__ = [
    'qmlParser',
    'qmlSemantics',
    'main'
]


class qmlParser(Parser):
    def __init__(self,
                 whitespace=None,
                 nameguard=None,
                 comments_re='\\(\\*.*?\\*\\)',
                 eol_comments_re='#.*?$',
                 ignorecase=None,
                 left_recursion=True,
                 **kwargs):
        super(qmlParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            **kwargs
        )

    @graken()
    def _component_type_(self):
        self._pattern(r'[A-Z][a-z0-9]*')

    @graken()
    def _property_type_(self):
        self._pattern(r'[a-zA-Z0-9_]+')

    @graken()
    def _identifier_(self):
        self._pattern(r'[a-z][a-z0-9_]*')

    @graken()
    def _number_(self):
        self._pattern(r'[0-9]+(\.[0-9]+)?')

    @graken()
    def _property_declaration_(self):
        self._token('property')
        self._property_type_()
        self._identifier_()

    @graken()
    def _declaration_end_(self):
        self._token(';')

    @graken()
    def _property_assignment_(self):
        self._identifier_()
        self._token(':')
        self._expr_()

    @graken()
    def _expr_(self):
        with self._choice():
            with self._option():
                self._token('true')
            with self._option():
                self._token('false')
            with self._option():
                self._number_()
            with self._option():
                self._component_declaration_()
            self._error('expecting one of: false true')

    @graken()
    def _scope_declaration_(self):
        with self._group():
            with self._choice():
                with self._option():
                    self._property_declaration_()
                with self._option():
                    self._property_assignment_()
                with self._option():
                    self._component_declaration_()
                self._error('no available options')

    @graken()
    def _component_scope_(self):
        self._token('{')

        def block0():
            self._scope_declaration_()
        self._closure(block0)
        self._token('}')

    @graken()
    def _component_declaration_(self):
        self._component_type_()
        self._component_scope_()


class qmlSemantics(object):
    def component_type(self, ast):
        return ast

    def property_type(self, ast):
        return ast

    def identifier(self, ast):
        return ast

    def number(self, ast):
        return ast

    def property_declaration(self, ast):
        return ast

    def declaration_end(self, ast):
        return ast

    def property_assignment(self, ast):
        return ast

    def expr(self, ast):
        return ast

    def scope_declaration(self, ast):
        return ast

    def component_scope(self, ast):
        return ast

    def component_declaration(self, ast):
        return ast


def main(filename, startrule, trace=False, whitespace=None, nameguard=None):
    import json
    with open(filename) as f:
        text = f.read()
    parser = qmlParser(parseinfo=False)
    ast = parser.parse(
        text,
        startrule,
        filename=filename,
        trace=trace,
        whitespace=whitespace,
        nameguard=nameguard)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import string
    import sys

    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in qmlParser.rule_list():
                print(r)
            print()
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Simple parser for qml.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-n', '--no-nameguard', action='store_true',
                        dest='no_nameguard',
                        help="disable the 'nameguard' feature")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('-w', '--whitespace', type=str, default=string.whitespace,
                        help="whitespace specification")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(
        args.file,
        args.startrule,
        trace=args.trace,
        whitespace=args.whitespace,
        nameguard=not args.no_nameguard
    )
