def main():
    horiz = 0
    depth = 0
    f = open("day2.txt", "r")
    for x in f.readlines():
        x = x.rstrip()
        y = x.split(" ")
        if "forward" in x:
            horiz += int(y[1])
        elif "up" in x:
            depth -= int(y[1])
        elif "down" in x:
            depth += int(y[1])
    print(horiz * depth)

if __name__ == "__main__":
    main()