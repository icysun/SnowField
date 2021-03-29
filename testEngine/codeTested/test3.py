# 任意代码执行

cmd1, cmd2, cmd3 = input('cmd1'), input('cmd2'), input('cmd3')
exec(cmd1)
exec(cmd2)
system(cmd3)