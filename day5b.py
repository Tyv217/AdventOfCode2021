import math

def main():
    input = open("input/day5.txt").read().split("\n")
    grid = set()
    moreThanOne = set()
    for line in input:
        x1 = int(line.split(" -> ")[0].split(",")[0])
        y1 = int(line.split(" -> ")[0].split(",")[1])
        x2 = int(line.split(" -> ")[1].split(",")[0])
        y2 = int(line.split(" -> ")[1].split(",")[1])
        if(x1 == x2):
            for y in range(min(y1,y2), max(y1,y2) + 1):
                if((x1,y) in grid):
                    moreThanOne.add((x1,y))
                else:
                    grid.add((x1,y))
        elif(y1 == y2):
            for x in range(min(x1,x2), max(x1,x2) + 1):
                if((x,y1) in grid):
                    moreThanOne.add((x,y1))
                else:
                    grid.add((x,y1))
        elif(abs(x1 - x2) == abs(y1 - y2)):
            if(x1 > x2):
                tmp1, tmp2 = x1, y1
                x1, y1 = x2, y2
                x2, y2 = tmp1, tmp2
            for x in range(x1, x2+1):
                if((x,y1) in grid):
                    moreThanOne.add((x,y1))
                else:
                    grid.add((x,y1))
                if(y1 > y2):
                    y1 -= 1
                else:
                    y1 += 1
    print(len(moreThanOne))
                

if __name__ == "__main__":
    main()