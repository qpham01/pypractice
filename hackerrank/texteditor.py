# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
from turtle import undo


def text_editor(string, commands):
    undoStack = deque()
    results = []
    for command in commands:       
        cmdList = command.split()
        cmd = int(cmdList[0])
        if len(cmdList) > 1:
            param = cmdList[1]
        else:
            param = None
        
        if cmd == 1:
            undoStack.append(string)
            string += param
            continue
        
        if cmd == 2:
            undoStack.append(string)
            size = len(string)
            intParam = int(param)
            string = string[:size - intParam]
            continue
        
        if cmd == 3:
            intParam = int(param)
            results.append(string[intParam - 1])
            continue
            
        if cmd == 4:
            if len(undoStack) > 0:
                string = undoStack.pop()
            continue
    return results