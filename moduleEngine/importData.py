from json import loads
from logEngine.consoleLog import logFuncImport

def importFuncs(modulePath: str):
    taintedFuncData = {}
    taintedFuncs = loads(open('./moduleEngine/{}/taintedFunc.json'.format(modulePath), encoding="utf8").read())
    for func in taintedFuncs:
        funcName, info = func, taintedFuncs[func]
        funcId = modulePath + '/' + funcName
        description = info['description']
        taintedFuncData[funcName] = {'funcId': funcId, 'description': description}
        logFuncImport(funcId, description)
    taintSourceData = {}
    taintSources = loads(open('./moduleEngine/{}/taintSource.json'.format(modulePath), encoding="utf8").read())
    for func in taintSources:
        funcName, info = func, taintSources[func]
        funcId = modulePath + '/' + funcName
        description = info['description']
        logFuncImport(funcId, description)
        taintSourceData[funcName] = {'funcId': funcId, 'description': description}
    sinkFuncData = {}
    sinkFuncs = loads(open('./moduleEngine/{}/sinkFunc.json'.format(modulePath), encoding="utf8").read())
    for func in sinkFuncs:
        funcName, info = func, sinkFuncs[func]
        funcId = modulePath + '/' + funcName
        description = info['description']
        logFuncImport(funcId, description)
        taintSourceData[funcName] = {'funcId': funcId, 'description': description}
    return taintedFuncData, taintSourceData, sinkFuncData