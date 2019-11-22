import load_input

def step(v, x, y):
    if v == 'v':
        y -=1
    elif v == '>':
        x +=1
    elif v == '<':
        x -=1
    elif v == '^':
        y +=1
    return x, y

def upd(houses, x, y):
    houses[x] = houses.get(x, set())
    houses[x].add(y)

content = load_input.load(2015, 3)


houses = {}
x1 = 0
y1 = 0
x2 = 0
y2 = 0
houses[x1] = houses.get(x1, set())
houses[x1].add(y1)
odd = False

for v in content:
    odd = not odd
    if odd:
        x1, y1 = step(v, x1, y1)
        upd(houses, x1, y1)
    else:
        x2, y2 = step(v, x2, y2)
        upd(houses, x2, y2)

num = 0
for x in houses.keys():
    num += len(houses[x])

print(num)
