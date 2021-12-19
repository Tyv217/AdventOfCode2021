from pprint import pprint

def return_mapping(signals):
    signal_mapping = {}
    remaining = set()
    for x in signals.split(" "):
        if len(x) == 2:
            signal_mapping[1] = set(char for char in x)
        elif len(x) == 3:
            signal_mapping[7] = set(char for char in x)
        elif len(x) == 4:
            signal_mapping[4] = set(char for char in x)
        elif len(x) == 7:
            signal_mapping[8] = set(char for char in x)
        else:
            remaining.add(x)
    a = list(set(char for char in signal_mapping[7]) - set(char for char in signal_mapping[1]))[0]
    bd = list(set(char for char in signal_mapping[4]) - set(char for char in signal_mapping[1]))
    b = bd[0]
    d = bd[1]
    signal569 = []
    for x in remaining:
        if b in x and d in x:
            signal569.append(x)
    for x in signal569:
        if len(x) == 5:
            signal_mapping[5] = set(char for char in x)
        else:
            if len(set(char for char in signal_mapping[4]) - set(char for char in x)) > 0:
                signal_mapping[6] = set(char for char in x)
            else:
                signal_mapping[9] = set(char for char in x)
    for x in remaining:
        if x not in signal569:
            if len(set(char for char in signal_mapping[1]) - set(char for char in x)) == 0:
                if len(x) == 5:
                    signal_mapping[3] = set(char for char in x)
                else:
                    signal_mapping[0] = set(char for char in x)
            else:
                signal_mapping[2] = set(char for char in x)
    return signal_mapping




def main():
    input = open("input/day8.txt").read().split("\n")
    counter = 0
    for x in input:
        signals = x.split("|")
        mapping = return_mapping(signals[0].strip())
        four_digits = signals[1].lstrip().split(" ")
        code = ""
        for y in range(4):
            digit = set(char for char in four_digits[y])
            for z in mapping.keys():
                if mapping[z] == digit:
                    code += str(z)
        counter += int(code)
    print(counter)

if __name__ == "__main__":
    main()