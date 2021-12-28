gamma = []
epsilon = []
gamma_dec = 0
epsilon_dec = 0
for x in range(12):
    zero = 0
    one = 0
    with open("input.txt") as f:
        for i, l in enumerate(f):
            if l[x] == "0":
                zero += 1
            if l[x] == "1":
                one += 1
        if zero > one:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)
    power = 11
    gamma_dec += gamma[x] * (2 ** (power-x))
    epsilon_dec += epsilon[x] * (2 ** (power-x))
print(gamma_dec * epsilon_dec)