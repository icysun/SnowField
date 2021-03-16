from testEngine.unitTest import unitTest
from testEngine.funcTest import funcTest

def banner():
    banner = """
  ▄▄▄▄                       ▄▄▄▄▄▄   ▀    ▀▀█               █ 
 █▀   ▀ ▄ ▄▄    ▄▄▄  ▄     ▄ █      ▄▄▄      █     ▄▄▄    ▄▄▄█ 
 ▀█▄▄▄  █▀  █  █▀ ▀█ ▀▄ ▄ ▄▀ █▄▄▄▄▄   █      █    █▀  █  █▀ ▀█ 
     ▀█ █   █  █   █  █▄█▄█  █        █      █    █▀▀▀▀  █   █
 ▀▄▄▄█▀ █   █  ▀█▄█▀   █ █   █      ▄▄█▄▄    ▀▄▄  ▀█▄▄▀  ▀█▄██  雪原：Python代码静态漏洞扫描器

    """
    print(banner)

if __name__ == "__main__":
    banner()
    funcTest()
    unitTest(1)