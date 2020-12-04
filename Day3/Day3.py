def part1():
    input = open("input.txt")
    ln = 1
    x = 0
    counter = 0
    for line in input:
        line = line.rstrip()
        #print("line:",ln, "pos:", x)
        if ln > 1:
            #print(line[x])
            if line[x] == "#":
                counter += 1
            #print(counter)
        x = x + 3
        if x > 30:
            x = x-31
        ln += 1
    return counter

print(part1()) 


def part2a():
    horizontaljumps =[1,3,5,7]
    multiplier = 1
    for i in horizontaljumps:
        input = open("input.txt")
        ln = 1
        x = 0
        counter = 0
        for line in input:
            line = line.rstrip()
            if ln > 1:
                if line[x] == "#":
                    counter += 1
            x = x + i
            if x > 30:
                x = x-31
            ln += 1
        multiplier = multiplier * counter
    return multiplier

def part2b():
    input = open("input.txt")
    ln = 1
    x = 0
    counter = 0
    for line in input:
        line = line.rstrip()
        if ln > 1 and (ln % 2) == 1:
            x = x + 1
            if x > 30:
                x = x-31
            #print("line:",ln, "pos:", x)
            #print(line[x])
            if line[x] == "#":
                counter += 1
            #print(counter)
        ln += 1
    return counter

print(part2a() * part2b())
