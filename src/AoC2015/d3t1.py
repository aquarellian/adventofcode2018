import load_input
content = load_input.load(2015, 3)

houses = {}
x = 0
y = 0
houses[x] = houses.get(x, set())
houses[x].add(y)

for v in content:
    if v == 'v':
        y -=1
    elif v == '>':
        x +=1
    elif v == '<':
        x -=1
    elif v == '^':
        y +=1
    houses[x] = houses.get(x, set())
    houses[x].add(y)

num = 0
for x in houses.keys():
    num += len(houses[x])

print(num)
