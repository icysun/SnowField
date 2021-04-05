from os import system

taint1, taint2 = sink(input('taint1')), input('taint2')
system(taint1)
system(taint2)