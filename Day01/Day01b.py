group = []
increased = 0
with open('input.txt') as f:
    input = f.readlines()

    for i, l in enumerate(input):
        if i>1:      
            group.append(int(l) + int(input[i-1]) + int(input[i-2]))

    for i, l in enumerate(group):
        if i>0 and pre<int(l):
            increased+=1
        pre=int(l)
print(increased)