def main():
    f = open("day3.txt", "r")
    lines = f.readlines()
    bitPosition = 0
    while(len(lines) > 1):
        newLines = []
        ones = 0
        zeros = 0
        common = ""
        for x in lines:
            if(x[bitPosition] == "0"):
                zeros += 1
            elif(x[bitPosition] == "1"):
                ones += 1
        if zeros > ones:
            common = "0"
        else:
            common = "1"
        for x in lines:
            if(x[bitPosition] == common):
                newLines.append(x)
        lines = newLines
        bitPosition += 1
    f = open("day3.txt", "r")
    lines1 = f.readlines()
    bitPosition = 0
    while(len(lines1) > 1):
        newLines = []
        ones = 0
        zeros = 0
        uncommon = ""
        for x in lines1:
            if(x[bitPosition] == "0"):
                zeros += 1
            elif(x[bitPosition] == "1"):
                ones += 1
        if zeros > ones:
            uncommon = "1"
        else:
            uncommon = "0"
        for x in lines1:
            if(x[bitPosition] == uncommon):
                newLines.append(x)
        lines1 = newLines
        bitPosition += 1
    oxgen = int(lines[0].rstrip(),2)
    co2 = int(lines1[0].rstrip(),2)
    print(oxgen * co2)

if __name__ == "__main__":
    main()