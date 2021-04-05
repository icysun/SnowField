from os import system

taint3 = input('taint3')
taint1, taint2 = sink(taint3), input('taint2')
system(taint1)
system(taint2)