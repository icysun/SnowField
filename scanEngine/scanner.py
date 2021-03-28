from cfgEngine import CFGBuilder, Block, Link, CFG
from moduleEngine.importData import importFuncs
from logEngine.consoleLog import logScanResult, logStatement
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
        self.scanCache = set()

    def scan(self):
        self.generateCFG()
        self.funcDataInit()
        self.analyze(self.cfg)

    def generateCFG(self):
        self.cfg = CFGBuilder().build_from_src(self.name, self.code)
        self.cfg.build_visual('./scanEngine/cfgGenerated/{}/{}'.format(self.name, self.name))

    def funcDataInit(self):
        for modulePath in self.modulePath:
            self.taintedFuncs, self.taintSources, self.sinkFuncs = importFuncs(modulePath)

    def analyze(self, cfg):
        for block in cfg.__iter__():
            for func_call in block.func_calls:
                if func_call in self.taintedFuncs.keys():
                    #logStatement(block.statements[0])
                    self.trace(block, func_call, block.func_calls[func_call]['args'])
                    for taintSource in self.scanCache:
                        logScanResult(self.taintedFuncs[func_call]['description'], str(taintSource), str(block))
                    self.scanCache.clear()

    def trace(self, currentBlock: Block, func_call, args):
        for predecessor in currentBlock.predecessors:
            if predecessor.isLoopBack == True:
                continue
            if predecessor.source.id > predecessor.target.id:
                predecessor.isLoopBack = True
            preBlock = predecessor.source
            statement = preBlock.statements[0]
            if self.is_tainted_statement(statement, args):
                self.scanCache.add(preBlock)
            else:
                self.trace(preBlock, func_call, args)

    def is_tainted_statement(self, statement, args):
        #logStatement(statement)
        if type(statement) == ast.Assign:
            logStatement(statement)
            if statement.targets[0].id in args:
                if type(statement.value) == ast.Call:
                    funcName = statement.value.func.id
                    if funcName in self.taintSources:
                        return True
        return False