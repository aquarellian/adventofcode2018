class Group:
    def __init__(self, id, side, units, hp, weaknesses, immunities, attack, damage, initiative):
        self.id = id
        self.side = side
        self.units = units
        self.hp = hp
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.attack = attack
        self.damage = damage
        self.initiative=initiative

def substr_between(line, start_mrk, end_mrk):
    if start_mrk is None or start_mrk in line:
        start = 0 if start_mrk is None else line.index(start_mrk) + len(start_mrk)
    else:
        return None
    end = len(line) if end_mrk is None else line.index(end_mrk, start)
    return line[start:end]


def calculate_damage(aggressor, victim):
    if victim is None:
        return 0
    if aggressor.attack in victim.immunities:
        return 0
    elif aggressor.attack in victim.weaknesses:
        return 2 * aggressor.units * aggressor.damage
    else:
        return aggressor.units * aggressor.damage


def choose_target(group, groups, chosen):
    enemies = [g for g in groups if g.side != group.side and not group.attack in g.immunities and not g in chosen]
    enemies = sorted(enemies, key=lambda g: g.initiative, reverse=True)
    enemies = sorted(enemies, key=lambda g: g.units * g.damage, reverse=True)
    enemies = sorted(enemies, key=lambda g: calculate_damage(group, g), reverse=True)
    return None if len(enemies) == 0 or calculate_damage(group, enemies[0])==0 else enemies[0]

def emulate_fight(groups, boost=0):
    has_enemies = True
    active_groups = []
    for g in groups:
        if g.side == 'G':
            g.damage += boost

    while has_enemies:
        print('Immune System:')
        for g in groups:
            if g.units > 0 and g.side == 'G':
                print('Group ', g.id, ' contains ', g.units, ' units')
        print('Infection:')
        for g in groups:
            if g.units > 0 and g.side == 'B':
                print('Group ', g.id, ' contains ', g.units, ' units')


        active_groups = [g for g in groups if g.units > 0]
        active_groups = sorted(active_groups, key=lambda g: g.initiative, reverse=True)
        active_groups = sorted(active_groups, key=lambda g: g.units * g.damage, reverse=True)
        combats = {}
        for g in active_groups:
            has_enemies &= len([gr for gr in active_groups if gr.side != g.side and g.units > 0]) > 0
            enemy = choose_target(g, active_groups, combats.values())
            combats[g] = enemy
            if enemy is not None:
                print('Immune System group ' if g.side == 'G' else 'Infection group ', g.id, ' would deal defending group ', enemy.id, ' ', calculate_damage(g, enemy), ' damage')
        initiative_groups = sorted(active_groups, key=lambda g: g.initiative, reverse=True)
        for g in initiative_groups:
            enemy = combats[g]
            if enemy is not None:
                total_damage = calculate_damage(g, enemy)
                units_killed = total_damage // enemy.hp
                print('Immune group ' if g.side == 'G' else 'Infection group ', g.id, ' attacks defending group ', enemy.id, ' killing ', min(units_killed, enemy.units))
                enemy.units = max(0, enemy.units - units_killed)
                if enemy.units == 0:
                    active_groups.remove(enemy)
        print()
    side = active_groups[0].side
    units = sum([gr.units for gr in active_groups])
    return side, units

with open("../resources/task47.txt") as f:
    content = f.readlines()
    side = None
    groups = []
    id = None
    for line in content:
        if 'Immune System:' in line:
            side = 'G'
            id = 1
        elif 'Infection:' in line:
            side = 'B'
            id = 1
        elif 'units' in line:
            units = int(substr_between(line, None, ' '))
            hp = int(substr_between(line, 'units each with ', ' hit points'))
            details = substr_between(line, '(', ')').split(';') if '(' in line else []
            immunities = []
            weaknesses = []

            for det in details:
                if 'immune to ' in det:
                    sub = substr_between(det, 'immune to ', None)
                    immunities = [s.strip() for s in substr_between(det, 'immune to ', None).split(',')]
                if 'weak to ' in det:
                    weaknesses = [s.strip() for s in substr_between(det, 'weak to ', None).split(',')]

            damage = int(substr_between(line, 'with an attack that does ', ' '))
            attack = substr_between(line, 'does '+ str(damage), ' damage').strip()
            initiative = int(substr_between(line, 'initiative ', None).strip())
            group = Group(id, side, units, hp, weaknesses, immunities, attack, damage, initiative)
            id +=1
            groups.append(group)

    side, units = emulate_fight(groups)
    print(units)


# 26766 too high
# 26753


