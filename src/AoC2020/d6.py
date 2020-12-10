# task 1
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d6.txt") as f:
    content = f.read().split('\n\n')
    count = 0
    for gr in content:
        l = set()
        for ch in gr:
            if ch.isalpha():
                l.add(ch)
        count += len(l)
    print (count)

#task 2
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d6.txt") as f:
    content = f.read().split('\n\n')
    count = 0

    for gr in content:
        cnt = len(gr.split("\n")) #??
        arr = [None for x in range(26)]
        for ch in gr:
            if ch.isalpha():
                # print(ch, ord(ch), ord(ch) - 96)
                ind = ord(ch) - 97
                if arr[ind] is None:
                    arr[ind] = cnt - 1
                else:
                    arr[ind] -= 1
                if arr[ind] == 0:
                    count +=1
    print (count)
