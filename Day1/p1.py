f = open("p1_input.txt", "r")
count = 0
first = 0
prev = 0
for line in f:
    if first == 0:
        first = 1
    else:
        if int(line) > prev:
            count+=1 
    prev = int(line)
print(count)
f.close()