def score(row, called):
    return len(set(row).intersection(called))

def win(board, called):
    for r in board:
        if score(r, called) == 5:
            return True
    for c in zip(*board):
        if score(c, called) == 5:
            return True
    return False

def main():
    input = open("input/day4.txt").read().split("\n\n")
    called = set()
    breakOut = False
    boards = list([list(l.split()) for l in b.splitlines()] for b in input[1:])
    for n in input[0].split(","):
        called.add(n)
        for b in boards:
            if win(b, called):
                uncalled = list(set(item for row in b for item in row) - set(called))
                sum = 0
                for num in uncalled:
                    sum += int(num)
                print(sum * int(n))
                breakOut = True
                break
        if breakOut:
            break

if __name__ == "__main__":
    main()