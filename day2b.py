def main():
    horiz = 0
    depth = 0
    aim = 0
    f = open("input/day2.txt", "r")
    for x in f.readlines():
        x = x.rstrip()
        y = x.split(" ")
        if "forward" in x:
            horiz += int(y[1])
            depth += aim * int(y[1])
        elif "up" in x:
            aim -= int(y[1])
        elif "down" in x:
            aim += int(y[1])
    print(horiz * depth)

if __name__ == "__main__":
    main()