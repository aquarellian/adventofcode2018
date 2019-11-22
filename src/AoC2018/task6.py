with open("task5.test.txt") as f:
    content = f.readlines()
    queries = {}
    maybe = {}
    for claim in content:
        strs = claim.split(' ')
        id = int(strs[0].replace('#', ''))
        x = int(strs[2].replace(':', '').split(',')[0])
        y = int(strs[2].replace(':', '').split(',')[1])
        w = int(strs[3].split('x')[0])
        h = int(strs[3].split('x')[1])
        overlaps = False

        for i in range(x, x+w):
            if queries.get(i, None) is None:
                queries[i] = {}
            for j in range(y, y+h):
                queries[i][j] = 1 + queries[i].get(j,0)
                if queries[i][j] >= 2:
                    overlaps=True
        if not overlaps:
            maybe[id] = claim

    for id, claim in maybe.items():
        strs = claim.split(' ')
        id = int(strs[0].replace('#', ''))
        x = int(strs[2].replace(':', '').split(',')[0])
        y = int(strs[2].replace(':', '').split(',')[1])
        w = int(strs[3].split('x')[0])
        h = int(strs[3].split('x')[1])
        overlaps = False
        for i in range(x, x+w):
            for j in range(y, y+h):
                if queries[i][j] >= 2:
                    overlaps=True
                    break
            if overlaps:
                break
        if not overlaps:
            print(id)
            break


