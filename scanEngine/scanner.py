from cfgEngine import CFGBuilder
from moduleEngine.importData import importFuncs

class Scanner():

    def __init__(self, name ,code):
        self.name = name
        self.code = code
        self.cfg = None
        self.taintedFuncs = {}
        self.taintSources = {}
        self.sinkFuncs = {}
        self.modulePath = ['builtin']

    def scan(self):
        self.generateCFG()
        self.funcDataInit()
        self.analyze(self.cfg.entryblock)

    def generateCFG(self):
        self.cfg = CFGBuilder().build_from_src(self.name, self.code)
        self.cfg.build_visual('./scanEngine/cfgGenerated/{}/{}'.format(self.name, self.name))

    def funcDataInit(self):
        for modulePath in self.modulePath:
            self.taintedFuncs, self.taintSources, self.sinkFuncs = importFuncs(modulePath)

    def analyze(self, currentBlock):
        for i in currentBlock.func_calls:
            print(i)