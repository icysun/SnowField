from scanEngine.scanner import Scanner

def unitTest(testid : int):
    testname = 'test{}'.format(testid)
    code = open('./testEngine/codeTested/{}.py'.format(testname), encoding="utf8").read()
    testScanner = Scanner(testname, code)
    testScanner.scan()