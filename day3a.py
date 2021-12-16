def main():
    f = open("input/day3.txt", "r")
    gamma = 0
    epsilon = 0
    lines = f.readlines()
    bits = {}
    firstNum = lines[0].rstrip()
    length = len(firstNum)
    for i in range(length):
        bits[i] = {"0": 0, "1": 0}
    for x in lines:
        x = x.rstrip()
        for y in range(len(x)):
            if(x[y] == '0'):
                d = bits[y]
                d["0"] += 1
            elif(x[y] == '1'):
                d = bits[y]
                d["1"] += 1
    for x in bits.keys():
        d = bits[x]
        if d["1"] > d["0"]:
            gamma += (2 ** (length - 1 - int(x)))
        elif d["0"] > d["1"]:
            epsilon += (2 ** (length - 1 - int(x)))
    print(gamma * epsilon)

if __name__ == "__main__":
    main()