import time
from astpretty import pprint

def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def logProcess(info : str):
    print("[+] {} {}".format(getTime(), info))

def logStatus(info : str):
    print("[-] {} {}".format(getTime(), info))

def logFuncCall(info : str):
    print("[*] {} Call function: {}".format(getTime(), info))

def logFuncImport(funcId : str, description : str):
    print("[*] {} Import function: {}, \"{}\"".format(getTime(), funcId, description))

def logScanResult(description : str, taintSource, taintedFunc):
    print("[*] {}\n\t发现漏洞: \033[;31;48m{}\033[0m,\n\t污染源: {}\t污染位置: {}".format(getTime(), description, taintSource, taintedFunc))

def logStatement(statement):
    print('-----------')
    pprint(statement)