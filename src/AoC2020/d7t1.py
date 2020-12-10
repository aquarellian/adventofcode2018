import re
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d7.txt") as f:
    lines = f.readlines()
    map = {}
    for line in lines:
        key = line.split("bags")[0].strip()
        if key not in map:
            map[key] = set()
        words = line.split(" ")
        digit_found = False
        st = ''
        for word in words:
            if digit_found:
                if word.isdigit() or word.endswith("\n"):
                    st = st + ' ' + word
                    if "bag" in st:
                        v = st[:st.index("bag")].strip()
                        map[key].add(v)
                    st = ''
                else:
                    st = st + ' ' + word
            elif word.isdigit():
                digit_found = True
    print(map)
    result_set = set()
    result_set.add('shiny gold')
    changed = True
    while changed:
        changed = False
        for (key, value) in map.items():
            if key not in result_set and any(x in value for x in result_set):
                result_set.add(key)
                changed = True

    print(result_set)
    print(len(result_set) -1)


