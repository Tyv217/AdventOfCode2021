def main():
    input = open("input/day7.txt").read().split(",")
    max = 0
    minFuel = float('inf')
    for x in input:
        if(int(x) > max):
            max = int(x) 
    for x in range(max):
        fuel = 0
        finished = True
        for y in input:
            fuel += abs(x - int(y))
            if fuel > minFuel:
                finished = False
                break
        if finished:
            minFuel = fuel
    print(minFuel)

if __name__ == "__main__":
    main()