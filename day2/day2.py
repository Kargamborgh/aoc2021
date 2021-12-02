file = open("day2input.txt", "r")

lines = file.readlines()

forward = 'forward'
up = 'up'
down = 'down'

horizontal = 0
depth = 0
for line in lines:
    line = line.strip()
    if forward in line:
        horizontal += (int(line[-1]))
    elif up in line:
        depth -= (int(line[-1]))
    elif down in line:
        depth += (int(line[-1])) 
    print(f'command: {line}')
    print(f'horizontal: {horizontal}')
    print(f'depth: {depth}')
print(f'horizontal times depth: {horizontal * depth}')

# part 2

horizontal2 = 0
depth2 = 0
aim = 0
for line in lines:
    line = line.strip()
    if forward in line:
        horizontal2 += (int(line[-1]))
        depth2 += (aim*(int(line[-1])))
    elif up in line:
        aim -= (int(line[-1]))
    elif down in line:
        aim += (int(line[-1]))
    print(f'command: {line}')
    print(f'horizontal: {horizontal2}')
    print(f'depth: {depth2}')
    print(f'aim: {aim}')
print(f'aimed horizontal times depth: {horizontal2 * depth2}')