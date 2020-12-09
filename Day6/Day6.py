data = [line.strip() for line in open("input.txt", 'r')]
#data = ["abc","","a","b","c","","ab","ac","","a","a","a","a","","b"]
questions = "abcdefghijklmnopqrstuvwxyz"

def resetquestiondata():
    questiondata = []
    for question in questions:
        questiondata.append([question,0])
    return questiondata

def part1():
    counts = []
    counted = []
    counter = 0
    for answers in data:
        #print(answers)
        if answers == "":
            counts.append(counter)
            #print(counts)
            counted = []
            counter = 0
        else:
            for answer in answers:
                #print(answer)
                if answer not in counted:
                    #print(counted)
                    counted.append(answer)
                    counter += 1
                    #print(counted)
                    #print(counter)
    counts.append(counter)
    #print(counts)
    return sum(counts)

print(part1())

def part2():
    questiondata = resetquestiondata()
    counts = []
    counter = 0
    personcount = 0
    for answers in data:
        if answers == "":
            for question in questiondata:
                if question[1] == personcount:
                    counter += 1
            counts.append(counter)
            counter = 0
            personcount = 0
            questiondata = resetquestiondata()
        else:
            personcount += 1
            for question in questiondata:
                if question[0] in answers:
                    question[1] += 1
    for question in questiondata:
        if question[1] == personcount:
            counter += 1
    counts.append(counter)
    #print(counts)
    return sum(counts)

print(part2())