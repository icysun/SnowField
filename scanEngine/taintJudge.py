from logEngine.consoleLog import logStatement
import ast

def is_tainted_statement(scanner, statement, argName, preBlock):

    def target_value_assign(target, value):
        if target.id == argName:
            if type(value) == ast.Call:
                funcName = value.func.id
                if funcName in scanner.taintSources:
                    return True
                for arg in value.args:
                    if type(arg) == ast.Name:
                        scanner.trace(preBlock, arg.id)
        return False

    if type(statement) == ast.Assign:
        # cmd = input('cmd')
        # exec(cmd)
        if type(statement.targets[0]) == ast.Name:
            return target_value_assign(statement.targets[0], statement.value)
        # cmd1, cmd2, ... = input('cmd1'), input('cmd2'), ...
        # exec(cmd1)
        # exec(cmd2)
        # ...
        if type(statement.targets[0]) == ast.Tuple:
            targets = statement.targets[0].elts
            for index in range(len(targets)):
                if target_value_assign(targets[index], statement.value.elts[index]):
                    return True


    return False