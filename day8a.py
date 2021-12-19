def main():
    input = open("input/day8.txt").read().split("\n")
    counter = 0
    for x in input:
        signals = x.split("|")
        for y in signals[1].split(" "):
            if len(y) in [2,3,4,7]:
                counter += 1
    print(counter)

if __name__ == "__main__":
    main()