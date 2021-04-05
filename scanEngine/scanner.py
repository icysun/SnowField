from cfgEngine import CFGBuilder, Block, Link, CFG
from moduleEngine.importData import importFunc, importModule
from logEngine.consoleLog import logScanResult, logStatement, logProcess, logStatus
import ast
from scanEngine.taintJudge import is_tainted_statement
from scanEngine.sinkJudge import is_sink_statement

class Scanner():

    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.cfg = None
        self.taintedFuncs = {}
        self.taintSources = {}
        self.sinkFuncs = {}
        self.scanCache = set()

    def scan(self):
        self.generateCFG()
        self.funcDataInit()
        self.analyze(self.cfg)

    def generateCFG(self):
        self.cfg= CFGBuilder().build_from_src(self.name, self.code)
        self.cfg.build_visual('./scanEngine/cfgGenerated/{}/{}'.format(self.name, self.name))

    def funcDataInit(self):
        for function in self.cfg.functions:
            funcData = importFunc(function["funcPath"])
            functionName = function["funcName"]
            if funcData['type'] == 'T':
                self.taintedFuncs[functionName] = funcData
            elif funcData['type'] == 'S':
                self.sinkFuncs[functionName] = funcData
            elif funcData['type'] == 'O':
                self.taintSources[functionName] = funcData
        for module in self.cfg.modules:
            funcDataList = importModule(module["modulePath"], module["moduleName"])
            for funcKeyData in funcDataList:
                if funcKeyData[1]['type'] == 'T':
                    self.taintedFuncs[funcKeyData[0]] = funcKeyData[1]
                elif funcKeyData[1]['type'] == 'S':
                    self.sinkFuncs[funcKeyData[0]] = funcKeyData[1]
                elif funcKeyData[1]['type'] == 'O':
                    self.taintSources[funcKeyData[0]] = funcKeyData[1]

    def analyze(self, cfg):
        for block in cfg.__iter__():
            for func_call in block.func_calls:
                if func_call in self.taintedFuncs.keys():
                    #logStatement(block.statements[0])
                    for argName in block.func_calls[func_call]['args']:
                        logProcess("追踪函数: {}, 参数: {}".format(func_call, argName))
                        self.trace(block, argName)
                        for taintSource in self.scanCache:
                            logScanResult(self.taintedFuncs[func_call]['description'], str(taintSource), str(block))
                        self.scanCache.clear()

    def trace(self, currentBlock: Block, argName):
        for predecessor in currentBlock.predecessors:
            if predecessor.isLoopBack == True:
                continue
            if predecessor.source.id > predecessor.target.id:
                predecessor.isLoopBack = True
            preBlock = predecessor.source
            statement = preBlock.statements[0]
            # logStatement(statement)
            if is_sink_statement():
                break
            if is_tainted_statement(self,statement, argName, preBlock):
                self.scanCache.add(preBlock)
            else:
                self.trace(preBlock, argName)