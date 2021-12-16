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
    input = open("day4.txt").read().split("\n\n")
    called = set()
    boards = list([list(l.split()) for l in b.splitlines()] for b in input[1:])
    for n in input[0].split(","):
        called.add(n)
        if(len(boards) == 1 and win(boards[0], called)):
            uncalled = list(set(item for row in boards[0] for item in row) - set(called))
            sum = 0
            for num in uncalled:
                sum += int(num)
            print(sum * int(n))
            break
        newBoard = [b for b in boards if not win(b, called)]
        boards = newBoard

if __name__ == "__main__":
    main()