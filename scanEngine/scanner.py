from cfgEngine import CFGBuilder, Block, Link, CFG
from moduleEngine.importData import importFuncs
from logEngine.consoleLog import logScanResult
import ast

class Scanner():

    def __init__(self, name, code):
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

    def analyze(self, currentBlock: Block):
        for func_call in currentBlock.func_calls:
            if func_call in self.taintedFuncs.keys():
                self.trace(currentBlock, func_call, currentBlock.func_calls[func_call]['args'])

    def trace(self, currentBlock, func_call, args):
        for statement in currentBlock.statements[::-1]:
            if type(statement) == ast.Assign:
                if statement.targets[0].id in args:
                    if type(statement.value) == ast.Call:
                        funcName = statement.value.func.id
                        if funcName in self.taintSources:
                            logScanResult(self.taintedFuncs[func_call]['description'])
