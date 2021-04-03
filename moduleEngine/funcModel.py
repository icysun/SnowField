import json
from moduleEngine.taintVector import vectorMultiply

class funcModel():
    def __init__(self, type, moduleName = None, funcName = None):
        self.type = type
        self.modelName = moduleName
        self.funcName = funcName

    def setModuleName(self, moduleName):
        self.modelName = moduleName

    def setFuncName(self, funcName):
        self.funcName = funcName

    def setDescription(self, description):
        self.description = description

    def setTaintVector(self, taintVector: list):
        self.taintVector = taintVector

    def modelStorage(self):
        data = {
            self.funcName:{
                "description": self.description,
                "type": self.type,
                "taintVector": self.taintVector
            }
        }

        filePath = "./{}/{}.json".format(self.modelName, self.funcName)
        with open(filePath, "w") as file:
            json.dump(data, file, ensure_ascii= False)