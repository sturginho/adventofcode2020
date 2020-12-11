data = [line.strip() for line in open("input.txt", 'r')]
#data = ["nop +0","acc +1","jmp +4","acc +3","jmp -3","acc -99","acc +1","jmp -4","acc +6"]


def part1():
    accumulator = 0
    pos = 0
    counted = []
    while pos < len(data) and pos not in counted:
        line = data[pos].split(" ")
        #print(line)
        if line[0] == "acc":
            accumulator += int(line[1])
            counted.append(pos)
            pos += 1
        elif line[0] == "jmp":
            counted.append(pos)
            pos += int(line[1])
        else:
            counted.append(pos)  
            pos += 1  
    return accumulator

print(part1())

def part2(data):
    def boot(data):
        accumulator = 0
        pos = 0
        counted = []
        while pos < len(data) and pos not in counted:
            line = data[pos].split(" ")
            #print(line)
            if line[0] == "acc":
                accumulator += int(line[1])
                counted.append(pos)
                pos += 1
            elif line[0] == "jmp":
                counted.append(pos)
                pos += int(line[1])
            else:
                counted.append(pos)  
                pos += 1  
        if pos == len(data):
            return accumulator
        else:
            return -1    
    ans = -1
    for i in range(len(data)):
        line = data[i].split(" ")
        #print("original line:",data[i])
        #if operation is not a increment
        if line[0] != 'acc':
            #for each of the jmp operation, if it starts switching, find acc
            data[i] = data[i].replace("nop","jmp") if line[0] == 'nop' else data[i].replace("jmp","nop")
            #print("new line:",data[i])
            ans = boot(data)
            #print(ans)
            data[i] = data[i].replace("nop","jmp") if line[0] == 'jmp' else data[i].replace("jmp","nop")
            #print("restored line:",data[i])
        if ans != -1:
            break
    return ans    

print(part2(data))