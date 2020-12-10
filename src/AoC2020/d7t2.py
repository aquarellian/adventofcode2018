def count_bags(key, map):
    counter = 0
    print(map[key])
    bags = map[key]
    if len(bags) == 0:
        return 0
    else:
        for (bag, cnt) in bags:
            counter = counter + cnt + cnt * count_bags(bag, map)
    return counter


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d7.txt") as f:
    lines = f.readlines()
    map = {}
    for line in lines:
        key = line.split("bags")[0].strip()
        if key not in map:
            map[key] = set()
        words = line.split(" ")
        digit = None
        st = ''
        for word in words:
            if digit is not None:
                if word.isdigit() or word.endswith("\n"):
                    st = st + ' ' + word
                    if "bag" in st:
                        v = st[:st.index("bag")].strip()
                        map[key].add((v, digit))
                    st = ''
                    if word.isdigit():
                        digit = int(word)
                else:
                    st = st + ' ' + word
            elif word.isdigit():
                digit = int(word)
    print(map)
    print(count_bags('shiny gold', map))











