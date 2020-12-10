with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d9.txt") as f:
    content = f.readlines()
    array = [int(x) for x in content]
    val = None
    mask_len = 25
    for i in range(mask_len, len(array)):
        mask = list(array[i-mask_len:i])
        val = array[i]
        found = False
        for mi in range(mask_len):
            m = mask[mi]
            maskcopy = mask.copy()
            maskcopy.remove(m)
            if val - m in maskcopy:
                found = True
                break
        if not found:
            print(val)
            break
    print(val)
    for i in range(len(array)):
        j = i
        l = list()
        subsum = 0
        while subsum < val:
            l.append(array[j])
            subsum += array[j]
            j += 1
        if subsum == val and not val in l:
            print(l)
            print(min(l) + max(l))
            break



