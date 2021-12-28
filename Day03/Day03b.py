def doSmth(input, mostCommon):
    for x in range(12):
        amount = sum(i[x] == '1' for i in input)
        if mostCommon == True:
            value = '1' if amount >= len(input) / 2 else '0'
        else:
            value = '0' if amount >= len(input) / 2 else '1'
        if len(input) > 1:
            input = [i for i in input if i[x] == value]
    return input[0]

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.readlines()
        oxygen = doSmth(input, True)
        co2 = doSmth(input, False)
    print(int(oxygen, 2) * int(co2, 2))