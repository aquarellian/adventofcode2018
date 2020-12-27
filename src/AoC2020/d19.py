def split_rule(s):
    if '((' in s:
        part1 = s[:s.index('((')]
        part2 = s[s.index('(('):s.index('))') +2]
        part3 = s[s.index('))') +2:]
        return split_rule(part1) + part2 + split_rule(part3)
    else:
        return s.split('|')




def calc(rules, key, depth, maxdepth):
    if '"' in rules[key]:
        return rules[key]
    if key == 8:
        v = calc(rules, 42, depth + 1, maxdepth).replace('"', '')
        rules[8] = '"((' + v + ')*)"'
        return rules[8]
    elif key == 11:
        v1 = calc(rules, 42, depth + 1, maxdepth).replace('"', '')
        v2 = calc(rules, 31, depth + 1, maxdepth).replace('"', '')
        rules[11] = '"((' + v1 + ')*(' + v2 + '))*"'
        return rules[11]
    elif ' | ' in rules[key]:
        keyrules = split_rule(rules[key])
    else:
        keyrules = [rules[key]]
    arr = []

    for keyrule in keyrules:
        rule = keyrule.strip().split(" ")
        s = []
        for r in rule:
            v = calc(rules, int(r), depth + 1, maxdepth).replace('"', '')
            if len(s) == 0:
                s = set([x.strip() for x in split_rule(rules[key])])
            else:
                s = set([x.strip() + y.strip()
                         for x in s if len(x) < maxdepth
                         for y in split_rule(rules[key]) if len(y) < maxdepth])
        arr += list(s)
    rules[key] = " | ".join(['"' + s + '"' for s in set(arr)])
    return rules[key]


import re


def check(rule, line):
    # options = [x.replace('"', '') for x in rule.split(" | ")]
    # return line in options
    pattern = "^" + rule.replace(" ", "") + "$"
    return re.match(pattern, line) is not None


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d19.txt") as f:
    content = f.readlines()
    rules = dict()

    for i in range(len(content)):
        line = content[i]
        if ':' in line:
            key = int(line[:line.index(':')])
            rules[key] = line[line.index(':') + 2:].strip()
        elif line.strip() == '':
            break
    lines = content[i + 1:]
    max_length = max([len(x.strip()) for x in lines])
    res = 0
    rule = calc(rules, 0, 0, max_length)
    options = set([x.replace('"', '') for x in rule.split(" | ")])
    for line in lines:
        res += int(line.strip() in options)
    print(res)

    # year = "^[0-9]{4}$"
