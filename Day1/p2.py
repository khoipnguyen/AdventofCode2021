f = open("p2_input.txt", "r")
count = 0 
three_back = 0
two_back = 0
one_back = 0
three_yet = 0
for line in f:
    if three_yet == 0:
        three_back = int(line)
        three_yet += 1
    elif three_yet == 1:
        two_back = int(line)
        three_yet += 1
    elif three_yet == 2:
        one_back = int(line)
        three_yet += 1
    else:
        if (three_back + two_back + one_back) < (two_back + one_back + int(line)):
            count += 1
        three_back = two_back
        two_back = one_back
        one_back = int(line)
print(count)
f.close()