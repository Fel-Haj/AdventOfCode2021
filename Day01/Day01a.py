counter = 0
with open('input.txt') as f:
    for i, l in enumerate(f.readlines()):
        if i > 0 and pre < int(l):
            counter += 1
        pre = int(l)
print(counter)