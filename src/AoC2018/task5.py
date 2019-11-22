with open("task5.txt") as f:
    content = f.readlines()
    queries = {}
    overlaps = 0
    for claim in content:
        strs = claim.split(' ')
        x = int(strs[2].replace(':', '').split(',')[0])
        y = int(strs[2].replace(':', '').split(',')[1])
        w = int(strs[3].split('x')[0])
        h = int(strs[3].split('x')[1])


        for i in range(x, x+w):
            if queries.get(i, None) is None:
                queries[i] = {}
            for j in range(y, y+h):
                queries[i][j] = 1 + queries[i].get(j,0)
                if queries[i][j] == 2:
                    overlaps+=1
    print(queries)
    print(overlaps)


