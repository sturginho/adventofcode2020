input = open("input.txt")
inputlist = []
for line in input:
    line = line.rstrip()
    line = int(line)
    inputlist.append(line)
#print(inputlist)

i = 0
l = (len(inputlist))
go = True

while i < l:
    a = 1
    while a < l:
        b = 2
        while b < l:
            if inputlist[i] + inputlist[a] + inputlist[b] == 2020:
                print(inputlist[i])
                print(inputlist[a])
                print(inputlist[b])
                print(inputlist[i] * inputlist[a] * inputlist[b])
                go = False
                break
            b += 1
        if not go:
            break
        a += 1
    if not go:
        break
    i += 1

print ("end")