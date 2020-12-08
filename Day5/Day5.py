def getseats():
    seats = []
    data = [line.strip() for line in open("input.txt", 'r')]
    for line in data:
        rownumber = 0
        colnumber = 0
        rows = [row for row in range(0, 128)]
        cols = [col for col in range(0, 8)]
        for x in line:
            if x == 'F':
                a = 0
                b = int(len(rows)/2)
                rows = rows[a:b]
            elif x == 'B':
                a = int(len(rows)/2)
                b = len(rows)
                rows = rows[a:b]
            else:
                rownumber = rows[0]
                if x == 'L':
                    a = 0 
                    b = int(len(cols)/2)
                    cols = cols[a:b]
                    if len(cols) == 1:
                       colnumber = cols[0] 
                elif x == 'R':
                    a = int(len(cols)/2)
                    b = len(cols)
                    cols = cols[a:b]
                    if len(cols) == 1:
                       colnumber = cols[0] 
        seats.append(rownumber * 8 + colnumber)
    return seats

def part1():
    highseat = 0
    for seat in getseats():
        if seat > highseat:
            highseat = seat
    return highseat

print(part1())

def part2():
    possible_seats = [poss for poss in range(0, (part1()+1))]
    seats = getseats()
    candidate_seats = []
    myseat = ""
    for poss in possible_seats:
        if poss not in seats:
            candidate_seats.append(poss)
    #print(candidate_seats)
    for candidate in candidate_seats:
        a = candidate - 1
        b = candidate + 1
        if a in seats and b in seats:
            myseat = candidate
    return myseat

print(part2())