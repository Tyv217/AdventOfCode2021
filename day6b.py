from pprint import pprint
def main():
    input = open("input/day6.txt").read().split(",")
    fishes = {}
    for x in input:
        if int(x) in fishes.keys():
            fishes[int(x)] += 1
        else:
            fishes[int(x)] = 1
    for y in range(256):
        newFishes = {}
        for x in fishes.keys():
            if x == 0:
                newFishes[8] = fishes[0]
                if 6 in newFishes.keys():
                    newFishes[6] += fishes[0]
                else:
                    newFishes[6] = fishes[0]
            elif x == 7:
                if 6 in newFishes.keys():
                    newFishes[6] += fishes[7]
                else:
                    newFishes[6] = fishes[7]
            else:
                newFishes[x - 1] = fishes[x]
        fishes = newFishes
    sum = 0
    for x in fishes.keys():
        sum += fishes[x] 
    print(sum)

if __name__ == "__main__":
    main()