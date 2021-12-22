from queue import Queue

def main():
    input = open("input/day9.txt").read().split("\n")
    basins = []
    for x in range(len(input)):
        for y in range(len(input[x])):
            basin = 0
            coords_to_explore = Queue(0)
            coords_to_explore.put((x,y))
            visited = []
            visited.append((x,y))
            while(not coords_to_explore.empty()):
                (x1,y1) = coords_to_explore.get()
                basin += 1
                point = int(input[x1][y1])
                points = []
                if x1 != 0:
                    points.append((x1-1, y1))
                if x1 != len(input) - 1:
                    points.append((x1+1, y1))
                if y1 != 0:
                    points.append((x1, y1-1))
                if y1 != len(input[x]) - 1:
                    points.append((x1, y1+1))
                for (x2,y2) in points:
                    if int(input[x2][y2]) > point and int(input[x2][y2]) != 9:
                        if (x2,y2) not in visited:
                            coords_to_explore.put((x2,y2))
                            visited.append((x2,y2))
            basins.append(basin)
    basins.sort(reverse = True)
    print(basins[0] * basins[1] * basins[2])

if __name__ == "__main__":
    main()