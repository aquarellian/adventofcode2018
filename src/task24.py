with open("../resources/task23.txt") as f:
    content = f.readlines()
    plants = ''
    rules = {}
    generations = 102 ## this is a magic number after which pattern doesn't change, just move 1 step to right

    for line in content:
        if 'initial state: ' in line:
            plants = line[len('initial state: '):].strip()
        elif '=>' in line:
            rule = line[0: line.index(' ')]
            res = line[line.index('=> ')+3:].strip()
            if rule in rules:
                print('Duplicate rule found!!!')
                print(rule)
                print(rules[rule])
                print(res)
            rules[rule] = res
    plants = generations*'.' + plants + generations*'.'
    # print(plants)
    nextgen = ''
    all = set()
    pattern_starts = None
    for i in range(1, generations+1):
        for j in range(0, len(plants)):
            if j == 0:
                key = '..' + plants[:j+3]
            elif j == 1:
                key = '.' + plants[:j+3]
            elif j == len(plants) - 2:
                key = plants[j-2:len(plants)] + '.'
            elif j == len(plants) - 1:
                key = plants[j-2:len(plants)] + '..'
            else:
                key = plants[j-2:j+3]
            nextgen += rules.get(key, '.')

        plants = nextgen
        nextgen = ''

        stripped = plants.strip('.')
        if stripped not in all:
            all.add(stripped)
        else:
            pattern_starts = i
            break

    res = 0
    count = 0
    for i in range(0, len(plants)):
        if plants[i] == '#':
            res += (i-generations)
            count += 1

    print(count)
    print(res)

    target = 50000000000
    diff = count * (target-pattern_starts)
    print(diff)

    print(res + diff)

    # answer 2950000001598


