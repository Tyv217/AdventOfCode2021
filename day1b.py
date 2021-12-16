def main():
    f = open("input/day1.txt", "r")
    counter = 0
    lines = f.readlines()
    tmp = int(lines[0].rstrip())
    offset = 3
    for x in range(offset, len(lines)):
        y = int(lines[x].rstrip())
        if(y > tmp):
            counter += 1
        tmp = int(lines[x-2].rstrip())
    print(counter)

if __name__ == "__main__":
    main()