with open("resources/task9.txt") as f:
    content = f.readlines()
    line = content[0]
    i = 0
    # print(line)
    while i < len(line) - 1:
        ch1 = line[i]
        ch2 = line[i+1]
        if ch1.upper() == ch2.upper():
            # same letter, compare further
            if not ch1 == ch2:
                # different register, they collapse!!!!!
                line = line[:i]+ line[i+2:]
                # print(line)
                if i != 0:
                     i -=1
                     continue
        i+=1
    print(line)
    print(len(line))


