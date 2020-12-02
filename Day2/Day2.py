def part1():
    input = open("input.txt")
    validlines = 0
    for line in input:
        line = line.rstrip()
        ll = line.split(" ")
        policynum = ll[0].split("-")
        policymin = int(policynum[0])
        policymax = int(policynum[1])
        policyletter = ll[1][0]
        password = ll[2]
        counter = password.count(policyletter)
        if counter >= policymin and counter <= policymax:
            validlines += 1
    return validlines

def part2():
    input = open("input.txt")
    validlines = 0
    for line in input:
        line = line.rstrip()
        ll = line.split(" ")
        index1 = int(ll[0].split("-")[0])-1
        index2 = int(ll[0].split("-")[1])-1
        policyletter = ll[1][0]
        password = ll[2]
        checkstring = password[index1]+password[index2]
        counter = checkstring.count(policyletter)   
        if counter == 1:
            validlines += 1    
    return validlines

print ("Part1:",part1())
print ("Part2:",part2())