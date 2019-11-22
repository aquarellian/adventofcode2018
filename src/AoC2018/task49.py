def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2]) + abs(a[3]-b[3])

with open("../resources/task49.txt") as f:
    coords = []
    content = f.readlines()
    for line in content:
        coords.append(list(map(int, line.strip().split(','))))

    constellations = {}
    ind = 0
    for c in coords:
        cid = None
        deleted = set()
        for id, coordList in constellations.items():
            if id in deleted:
                continue
            for cc in coordList:
                if distance(c, cc) <=3:
                    if cid is None:
                        constellations[id].append(c)
                        cid = id
                    else:
                        constellations[cid] = constellations[cid] + constellations[id]
                        deleted.add(id)
                        # del constellations[id]
                    break
        for id in deleted:
            del constellations[id]
        if cid is None:
            constellations[ind] = [c]
            ind+=1
    print(len(constellations))





