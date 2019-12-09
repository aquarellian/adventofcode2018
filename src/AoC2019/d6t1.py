def count_orbits(d, key):
    if d.get(key) is not None:
        return 1 + count_orbits(d, d[key])
    return 0

def path_orbits(d, key):
    path=[]
    if d.get(key) is not None:
        path.append(key)
        path += path_orbits(d, d[key])
    return path

import load_input
content = load_input.load(2019, 6).split('\n')
# content='COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L'.split('\n')
# content = 'COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN'.split('\n')
d = {}
for line in content:
    if line == '':
        continue
    # print(line)
    data = line.split(')')
    # print(data)
    d[data[1]] = data[0]

# taskk1
# count = 0
# for key in d.keys():
#     count += count_orbits(d, key)
# print(count)

you = path_orbits(d, d['YOU'])
print(you)
san = path_orbits(d, d['SAN'])
print(san)

count = -1
for o in you:
    count +=1
    if o in san:
        count += san.index(o)
        print(count)
        break
