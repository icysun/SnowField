from os import system

taint1 = sink(input('taint1'))
system(taint1)