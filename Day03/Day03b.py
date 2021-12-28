with open("input.txt") as f:
    oxygen = f.readlines()
    for x in range(12):
        zero = 0
        for i, l in enumerate(oxygen):
            if l[x] == "0":
                zero += 1
        most_common = '0' if zero > len(oxygen)/2 else '1' 
        oxygen = [i for i in oxygen if most_common in i[x]]
        print("oxygen: ", oxygen)
        if len(oxygen) == 1:
            break
with open("input.txt") as f:    
    co2 = f.readlines()
    for x in range(12):
        zero = 0    
        for i, l in enumerate(co2):
            if l[x] == "0":
                zero += 1 
        least_common = '1' if zero > len(co2)/2 else '0'
        co2 = [line for line in co2 if least_common in line[x]]
        print("co2: ", co2)
        if len(co2) == 1:
            break
oxygen_dec = int(oxygen[0], 2)
co2_dec = int(co2[0], 2)
print(oxygen_dec, co2_dec)
print(oxygen_dec * co2_dec)