depth = 11394
target = [7,701]

# depth=510
# target=[10,10]
map = {}
def eroLevel(x,y):
    if x < len(map[y]):
        return map[y][x]
    if x == target[0] and y == target[1]:
        map[y][x]=0
    elif x ==0:
        if y==0:
            map[y][x]=0
        else:
            map[y][x]=(48271*y + depth) % 20183
    elif y == 0:
        map[y][x]=(16807*x + depth) % 20183
    else:
        map[y][x]=(eroLevel(x-1,y) * eroLevel(x,y-1) + depth) % 20183
    return map[y][x]

risk = 0
for i in range(0,target[1] + 1):
    map[i] = {}
    strng = ''
    for j in range(0, target[0]+1):
        # print(i,j)
        lvl = eroLevel(j, i) % 3
        risk += lvl
        strng += '.' if lvl == 0 else '|' if lvl ==2 else'='
    print(strng)
print(risk)
# 5645 too high


