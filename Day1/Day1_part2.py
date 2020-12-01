input = open("input.txt")
inputlist = []
for line in input:
    line = line.rstrip()
    line = int(line)
    inputlist.append(line)
#print(inputlist)

i = 0
l = (len(inputlist))
go = "yes"
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
                go = "no"
                break
            b += 1
        if go == "no":
            break
        a += 1
    if go == "no":
        break
    i += 1

print ("end")