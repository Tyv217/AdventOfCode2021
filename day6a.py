def main():
    input = open("input/day6.txt").read().split(",")
    for x in range(80):
        fish = []
        newFish = []
        for y in input:
            y = int(y)
            if(y == 0):
                fish.append(6)
                newFish.append(8)
            else:
                fish.append(y - 1)
        input = fish + newFish
    print(len(input))

if __name__ == "__main__":
    main()