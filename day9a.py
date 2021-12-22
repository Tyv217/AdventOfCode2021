def main():
    input = open("input/day9.txt").read().split("\n")
    counter = 0
    for x in range(len(input)):
        for y in range(len(input[x])):
            point = int(input[x][y])
            if x != 0 and int(input[x-1][y]) <= point:
                continue
            if x != len(input) - 1 and int(input[x+1][y]) <= point:
                continue
            if y != 0 and int(input[x][y-1]) <= point:
                continue
            if y != len(input[x]) - 1 and int(input[x][y+1]) <= point:
                continue
            counter += point
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()