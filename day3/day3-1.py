with open('day3/input', 'r') as input:
    maze = [line for line in input.read().splitlines()]

xpos = 0
xmove = 3
trees = 0

maze.pop(0) # we explicitly do not check the first line, so just get rid of it

for line in maze:
    xpos += xmove
    if line[xpos % len(line)] == '#':
        trees += 1

print(trees)
