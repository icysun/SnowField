from logEngine.consoleLog import logStatus

taintList = [
    "代码注入",
    "命令注入"
]

def vectorMultiply(vector1, vector2):
    newVector = []
    for index in range(len(vector1)):
        newVector.append(vector1[index] * vector2[index])
    return newVector