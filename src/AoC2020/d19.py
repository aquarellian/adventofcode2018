def split_rule(s):
    if '((' in s:
        part1 = s[:s.index('((')]
        part2 = s[s.index('(('):s.index(')+)') +3]
        part3 = s[s.index(')+)') +3:]
        arr = split_rule(part1) + [part2] + split_rule(part3)
        while '' in arr:
            arr.remove('')
        return arr
    else:
        return s.split('|')




def calc(rules, key, depth, maxdepth):
    if '"' in rules[key]:
        return rules[key]
    if key == 8:
        v = calc(rules, 42, depth + 1, maxdepth).replace('"', '')
        rules[8] = '"((' + v + ')+)"'
        return rules[8]
    elif key == 11:
        v1 = calc(rules, 42, depth + 1, maxdepth).replace('"', '')
        v2 = calc(rules, 31, depth + 1, maxdepth).replace('"', '')
        rules[11] = '"((' + v1 + '){1}(' + v2 + '){1}) | "' + '"((' + v1 + '){2}(' + v2 + '){2}) | "' + \
        '"((' + v1 + '){3}(' + v2 + '){3}) | "' + '"((' + v1 + '){4}(' + v2 + '){4}) | "' + \
        '"((' + v1 + '){5}(' + v2 + '){5}) | "' + '"((' + v1 + '){6}(' + v2 + '){6})"'
        return rules[11]
    elif key == 0:
        v1 = calc(rules, 8, depth + 1, maxdepth).replace('"', '')
        v2 = calc(rules, 11, depth + 1, maxdepth).replace('"', '')
        rules[0] = '(' + v1 +')(' + v2 + ')'
        return rules[0]
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
                s = set([x.strip() for x in split_rule(v)])
            else:
                s = set([x.strip() + y.strip()
                         for x in s if len(x) < maxdepth
                         for y in split_rule(v) if len(y) < maxdepth])
        arr += list(s)
    rules[key] = " | ".join(['"' + s + '"' for s in set(arr)])
    return rules[key]


import re


def check(rule, line):
    # options = [x.replace('"', '') for x in rule.split(" | ")]
    # return line in options
    pattern = "^(" + rule.replace('"', '').replace(" ", "") + ")$"
    return re.match(pattern, line) is not None


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d19_2.txt") as f:
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
        res += check(rule, line.strip())
        maxlen = max(maxlen, len(line.strip()))
        # res += int(line.strip() in options)
    print(res)

#441 high
#391 high
    # year = "^[0-9]{4}$"
