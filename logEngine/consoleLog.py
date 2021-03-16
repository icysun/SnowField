import time

def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def logProcess(info : str):
    print("[+] {} {}...".format(getTime(), info))

def logStatus(info : str):
    print("[-] {} {}".format(getTime(), info))

def logFunc(info : str):
    print("[*] {} Call function: {}".format(getTime(), info))