def main():
    f = open("input/day1.txt", "r")
    counter = 0
    tmp = 0
    for x in f.readlines():
        x = int(x.rstrip())
        if(x > tmp and tmp != 0):
            counter += 1
        tmp = x
    print(counter)

if __name__ == "__main__":
    main()