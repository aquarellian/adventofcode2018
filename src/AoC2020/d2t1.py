with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d2.txt") as f:
    content = f.readlines()

    valid = 0
    for line1 in content:
        if line1.find("-") == -1:
            print('error')
            break
        split1 = line1.split("-")
        minN = int(split1[0])
        split2 = split1[1].split(" ")
        maxN = int(split2[0])
        ch = split2[1].split(":")[0]
        pwd = split2[2]
        #cnt = len(pwd.split(ch)) - 1
        # if minN <= cnt <= maxN:
        #     valid+=1

        v1 = pwd[minN -1] == ch
        v2 = pwd[maxN -1] == ch if len(pwd) > maxN - 1 else False
        if v1 != v2:
            valid +=1
        elif len(pwd) > maxN + 1:
            print(line1, minN, maxN, ch, pwd, pwd[minN-1], pwd[maxN-1], v1, v2)
    print(valid)
    # 416 low

