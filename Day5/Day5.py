def part1():
    #data=['FBFBBFFRLR']
    seats = []
    highseat = 0
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
    for seat in seats:
        if seat > highseat:
            highseat = seat
    return highseat

print(part1())