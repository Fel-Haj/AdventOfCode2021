horizontal = 0
depth = 0
aim = 0
with open('input.txt') as f:
    for i, l in enumerate(f):
        value = l.split(" ", 1)
        if value[0] == "forward":
            horizontal += int(value[1])
            depth += aim * int(value[1])
        elif value[0] == "up":
            aim -= int(value[1])
        elif value[0] == "down":
            aim += int(value[1])
product = horizontal * depth
print(product)