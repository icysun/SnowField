from cfgEngine import CFGBuilder

def unitTest(testid : int):
    testname = 'test{}'.format(testid)
    code = open('./testEngine/codeTested/{}.py'.format(testname), encoding="utf8").read()
    cfg = CFGBuilder().build_from_src(testname, code)
    cfg.build_visual('./testEngine/cfgTested/{}/{}'.format(testname, testname))