class Ingredient:
    name = ''
    count = 0
    def __init__(self, name, count):
        self.name = name
        self.count = count

def parse_ing(st):
    count, name = st.strip().split(' ')
    return Ingredient(name, int(count))

def get_from_stash(extra, key, count):
    if key in extra.keys():
        ex = extra[key]
        if ex > count:
            extra[key] = ex - count
            print('untashing', count, key, 'left in stash:', extra[key] )
            return count
        else:
            extra[key] = 0
            print('untashing', ex, key, 'left in stash:', extra[key] )
            return ex
    return 0



import math
def disassemble_to_ore(book, key, count, extra):
    # look in the stash first
    stash = get_from_stash(extra, key, count)
    count -= stash

    if key == 'ORE':
        return count - stash
    elif count > 0: #stashed amt is not enough
        res = 0
        for i in range(1, len(book[key])):
            ing = book[key][i]
            k = 1 if book[key][i].count >= count else math.ceil(count / book[key][i].count)
            res += k * disassemble_to_ore(book, ing.name, ing.count, extra)
            # stash extra
            print('created ', ing.name, ing.count, count)
            if ing.count > count:
                extra[ing.name] = extra.get(ing.name, 0) + ing.count - count
                print('stashed', ing.name, ing.count - count)
        return int(res)
    return 0

import load_input
book = {}
# content = load_input.load(2019, 14).split('\n')

content = '10 ORE => 10 A\n1 ORE => 1 B\n7 A, 1 B => 1 C\n7 A, 1 C => 1 D\n7 A, 1 D => 1 E\n7 A, 1 E => 1 FUEL\n'.split('\n')
for line in content:
    if line != '':
        react2res = line.split('=>')
        res = parse_ing(react2res[1])
        book[res.name] = [res]

        for ing in react2res[0].split(','):
            _ing = parse_ing(ing)
            book[res.name].append(_ing)

fuel = book['FUEL']
if fuel[0].count != 1:
    print('want more fuel!')

count = disassemble_to_ore(book, 'FUEL', 1, {})
print(count)
#low 78567





