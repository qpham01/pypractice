from collections import deque

def swap(fullstack, emptystack):
    if len(fullstack) == 0:
        return
    emptystack.clear()
    for i in range(len(fullstack)):
        value = fullstack.pop()
        emptystack.append(value)
        
def processQueue(commands):
    stack1 = deque()
    stack2 = deque()
    results = []
    for command in commands:
        line = command.split()
        cmd = int(line[0])
    
        if cmd == 1:
            value = int(line[1])
            stack1.append(value)        
        
        if cmd == 2:
            if len(stack2) == 0:
                swap(stack1, stack2)
            if len(stack2) > 0:
                stack2.pop()
                        
        if cmd == 3:
            if len(stack2) == 0:
                swap(stack1, stack2)
            value = stack2.pop()
            results.append(value)
            stack2.append(value)
    return results