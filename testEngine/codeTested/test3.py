# 任意代码执行
import os
from os import system
from os import system as sys
import os as ooss

cmd1, cmd2, cmd3, cmd4 = input('cmd1'), input('cmd2'), input('cmd3'), input('cmd4')
sys(cmd1)
system(cmd2)
os.system(cmd3)
ooss.system(cmd4)