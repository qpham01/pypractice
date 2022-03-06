import heapq as hq

def fastheap(commands):
    data = []
    output = []
    dirty = False
    results = []

    for command in commands:
        line = command.split()
        cmd = int(line[0])
        
        if cmd == 1:
            value = int(line[1])
            hq.heappush(data, value)
            if len(output) == 0 or value < output[0]:
                dirty = True

        if cmd == 2:
            value = int(line[1])
            data.remove(value)
            if len(output) > 0 and value == output[0]:
                dirty = True
        
        if cmd == 3:
            if dirty:
                output = hq.nsmallest(1, data)
                dirty = False
            results.append(output[0])
    return results