from json import loads
from logEngine.consoleLog import logFuncImport

def importFuncs(modulePath: str):
    taintedFuncs = loads(open('./moduleEngine/{}/taintedFunc.json'.format(modulePath), encoding="utf8").read())
    for func in taintedFuncs:
        funcName, info = func, taintedFuncs[func]
        funcId = modulePath + '/' + funcName
        description = info['description']
        logFuncImport(funcId, description)
    taintSource = loads(open('./moduleEngine/{}/taintSource.json'.format(modulePath), encoding="utf8").read())
    for func in taintSource:
        funcName, info = func, taintSource[func]
        funcId = modulePath + '/' + funcName
        description = info['description']
        logFuncImport(funcId, description)