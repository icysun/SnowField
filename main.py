from astEngine.astGen import astGen

if __name__ == "__main__":
    file = open("./testEngine/codeTested/test0.py", encoding="utf8")
    code = file.read()
    astTree = astGen(code, print = True).astReturn()