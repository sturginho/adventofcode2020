data = [line.strip() for line in open("input.txt", 'r')]
#data = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]

def part1(preamble):
    pos = preamble
    ans = 0 
    while pos < len(data):
        previous = []
        curr = int(data[pos])
        #print("curr =",curr)
        for i in range(pos-preamble, pos):
            #print(data[i])
            previous.append(int(data[i]))
        #print(previous)
        x = 0
        l = len(previous)
        #print(l)
        go = True
        valid = False
        while x < l:
            a = 1
            while a < l:
                #print(previous[x],previous[a],previous[x] + previous[a])
                if previous[x] + previous[a] == curr:
                    valid = True
                    #print(valid)
                    go = False
                    #print(previous[x] + previous[a])
                a += 1
                if not go:
                    break
            x += 1
            if not go:
                break
        if valid:
            pos += 1
        else:
            #print("answer =",curr)
            ans = curr
            break
    return ans

print(part1(25))

def part2():
    pos = 0
    smallest = int(data[0])
    largest = int(data[0])
    acc = 0
    target = part1(25)
    ans = 0
    go = True
    while acc < target and go:
        acc = int(data[pos])
        #print(acc)
        for i in range(pos+1, len(data)):
            if int(data[i]) < smallest:
                smallest = int(data[i])
            if int(data[i]) > largest:
                largest = int(data[i])
            if acc + int(data[i]) == target:
                ans = smallest + largest
                print(smallest)
                print(largest)
                go = False
                break
            elif acc + int(data[i]) > target:
                acc = 0
                smallest = int(data[pos])
                largest = int(data[pos])
                break
            else: acc += int(data[i]) 
        pos +=1
    return ans

print(part2())