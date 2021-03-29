from json import loads
from logEngine.consoleLog import logFuncImport

def importFuncs(modulePath: str):
    taintedFuncData = {}
    data = open('./moduleEngine/{}/taintedFunc.json'.format(modulePath), encoding="utf8").read()
    if data:
        taintedFuncs = loads(data)
        for func in taintedFuncs:
            funcName, info = func, taintedFuncs[func]
            funcId = modulePath + '/' + funcName
            description = info['description']
            taintedFuncData[funcName] = {'funcId': funcId, 'description': description}
            logFuncImport(funcId, description)
    taintSourceData = {}
    data = open('./moduleEngine/{}/taintSource.json'.format(modulePath), encoding="utf8").read()
    if data:
        taintSources = loads(data)
        for func in taintSources:
            funcName, info = func, taintSources[func]
            funcId = modulePath + '/' + funcName
            description = info['description']
            logFuncImport(funcId, description)
            taintSourceData[funcName] = {'funcId': funcId, 'description': description}
    sinkFuncData = {}
    data = open('./moduleEngine/{}/sinkFunc.json'.format(modulePath), encoding="utf8").read()
    if data:
        sinkFuncs = loads(data)
        for func in sinkFuncs:
            funcName, info = func, sinkFuncs[func]
            funcId = modulePath + '/' + funcName
            description = info['description']
            logFuncImport(funcId, description)
            taintSourceData[funcName] = {'funcId': funcId, 'description': description}
    return taintedFuncData, taintSourceData, sinkFuncData