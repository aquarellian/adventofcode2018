def reaction(line):
    i = 0
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
    return len(line)

with open("resources/task9.txt") as f:
    content = f.readlines()
    line = content[0]
    import string
    abc = string.ascii_lowercase
    min = reaction(line)
    ch = None
    for i in range(0, 25):
        letter = abc[i]
        upd_ln = line.replace(letter, '')
        upd_ln = upd_ln.replace(letter.upper(), '')
        newmin = reaction(upd_ln)
        if newmin < min:
            min = newmin
            ch = letter
    print(ch)
    print(min)





