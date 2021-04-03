import json
from os import listdir

def importFunc(funcPath):
    path = './moduleEngine/' + funcPath.split(':')[0] + '/' + funcPath.split(':')[1] + '.json'
    data = open(path, 'r').read()
    return json.loads(data)[funcPath.split(':')[1]]

def importModule(modulePath, moduleName):
    path = './moduleEngine/' + modulePath
    functions = []
    for jsonFile in listdir(path):
        data = json.loads(open(path + '/' + jsonFile, 'r').read())
        if moduleName != '':
            moduleName += '.'
        functions.append([
            moduleName + jsonFile.split('.')[0] , data[jsonFile.split('.')[0]]
        ])
    return functions