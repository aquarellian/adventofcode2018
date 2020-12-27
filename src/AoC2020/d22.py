import queue
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d22.txt") as f:
    content = f.read().split("\n\n")
    arr1 = [int(x.strip()) for x in content[0].split("\n")[1:]]
    arr2 = [int(x.strip()) for x in content[1].split("\n")[1:]]
    q1 = queue.Queue()
    q2 = queue.Queue()
    for x in arr1:
        q1.put(x)
    for x in arr2:
        q2.put(x)
    while not (q1.empty() or q2.empty()):
        c1 = q1.get()
        c2 = q2.get()
        if c1 > c2:
            q1.put(c1)
            q1.put(c2)
        elif c1 < c2:
            q2.put(c2)
            q2.put(c1)
        else:
            print('even!')
    qwinner = q1 if q2.empty() else q2
    res = 0
    ind = qwinner.qsize()
    while not qwinner.empty():
        res += qwinner.get() * ind
        ind -=1
    print(res)







