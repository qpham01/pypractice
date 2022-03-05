def gridChallenge(grid):
    # Write your code here
    sortedGrid = []
    width = len(grid[0])
    for line in grid:
        row = []
        for c in line:
            row.append(c)
        row.sort()        
        sortedGrid.append(row)
    height = len(sortedGrid)
    good = True
    for c in range(width):
        previous = 'a'
        for r in range(height):
            current = sortedGrid[r][c]
            if current < previous:
                good = False
                break
            previous = current
        if not good:
            break
    output = "YES" if good else "NO"
    return output
            