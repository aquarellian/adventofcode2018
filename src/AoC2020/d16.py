with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d16.txt") as f:
    content = f.readlines()
    rules = dict()
    ind = 0
    while '' != content[ind].strip():
        line = content[ind]
        rule = line[:line.index(':')]
        v1 = int(line[line.index(':') + 2: line.index('-')].strip())
        v2 = int(line[line.index('-') + 1: line.index(' or ')].strip())
        v3 = int(line[line.index(' or ') + 4: line.rindex('-')].strip())
        v4 = int(line[line.rindex('-') + 1:].strip())
        rules[line[:line.index(':')]] = list([v1, v2, v3, v4])
        ind += 1
    ind +=2
    tickets = list()
    line = content[ind]
    tickets.append([int(x) for x in line.split(",")])
    ind += 3
    while ind < len(content):
        line = content[ind]
        tickets.append([int(x) for x in line.split(",")])
        ind += 1
    res = 0
    validated_tickets = list()
    for ticket in tickets:
        ticket_valid = True
        for v in ticket:
            rule_found = False
            for vs in rules.values():
                if vs[0]<= v <=vs[1] or vs[2]<= v <=vs[3]:
                    rule_found = True
                    break
            ticket_valid &= rule_found
            if not rule_found:
                res += v
        if ticket_valid:
            validated_tickets.append(ticket)
    print(res)
    print(len(validated_tickets))

    pos_to_rule = dict()
    for ticket in validated_tickets:
        for i in range(len(ticket)):
            v = ticket[i]
            can_add = False
            if i not in pos_to_rule:
                can_add = True
            for key, vs in rules.items():
                if vs[0]<= v <=vs[1] or vs[2]<= v <=vs[3]:
                    if i not in pos_to_rule:
                        pos_to_rule[i] = set()
                    if can_add:
                        pos_to_rule[i].add(key)
                elif i in pos_to_rule and key in pos_to_rule[i]:
                    pos_to_rule[i].remove(key)

    definite = False
    while not definite:
        definite = True
        for rule, indices in pos_to_rule.items():
            if len(pos_to_rule[rule]) == 1:
                ind = next(iter(pos_to_rule[rule]))
                for rule2 in pos_to_rule.keys():
                    if rule2 != rule and ind in pos_to_rule[rule2]:
                        pos_to_rule[rule2].remove(ind)
                        definite &= len(pos_to_rule[rule2]) == 1
        print(pos_to_rule)
    res = 1
    myticket = tickets[0]
    for pos, rules in pos_to_rule.items():
        rule = next(iter(pos_to_rule[pos]))
        if rule.startswith('departure'):
            res *= myticket[pos]
    print(res)





