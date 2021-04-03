from moduleEngine.funcModel import funcModel

'''
taintList = [
    "代码注入",
    "命令注入"
]
type:
    T : taintedFunctions
    S : sinkFunctions
    O : taintSource
'''

moduleName = "builtin"
funcName = "sinkCmdInjection"
description = "净化命令注入"
taintVector = [1, 0]
type = 'S'
funcData = funcModel(type, moduleName, funcName)
funcData.setDescription(description)
funcData.setTaintVector(taintVector)
funcData.modelStorage()