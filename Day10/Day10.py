#data = [16,10,15,5,1,11,7,19,6,12,4]

def part1():
    data = [int(line.strip()) for line in open("input.txt", 'r')]
    data.sort()
    data.append(max(data)+3)
    diff1 = 0
    diff3 = 0
    curr = 0
    for adapter in data:
        if adapter - curr == 1:
            diff1 += 1
        elif adapter - curr == 2:
            continue
        elif adapter - curr == 3:
            diff3 += 1
        else:
            print("SOmething's wrong!")
            break
        curr = adapter
    print(diff1)
    print(diff3)
    return diff1 * diff3

print(part1())

def part2():
    data = [int(line.strip()) for line in open("input.txt", 'r')]
    max_list = max(data) + 3
    data.append(max_list)
    data.append(0)
    data = sorted(data, reverse=True)

    to_end = {max_list: 1}

    for item in data[1:]:
        total = 0
        for i in range(3):
            if item + i + 1 in to_end:
                total += to_end[item + i + 1]

        to_end[item] = total

    return to_end[0]

print (part2())