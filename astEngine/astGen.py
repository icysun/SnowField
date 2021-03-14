from ast import parse
from astpretty import pprint

class astGen():
    def __init__(self, code, print = False):
        self.astGen(code)
        if print:
            self.astPrint()

    def astGen(self, code):
        self.ast = parse(code)

    def astPrint(self):
        pprint(self.ast)

    def astReturn(self):
        return self.ast
