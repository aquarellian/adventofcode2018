def get_color(x, y, w, h, content):
    idx = x + y * w
    while idx < len(content):
        if content[idx] == '0':
            return ' '
        elif content[idx] == '1':
            return '#'
        elif content[idx] == '2':
            idx += w*h
        else:
            print('error')


import load_input
content = load_input.load(2019, 8)
# content='0222112222120000'

layers = {}
w =  25
h =  6

color = None
s = ''
for y in range(0, h, 1):
    for x in range(0, w):
        c = get_color(x, y, w, h, content)
        s += str(c)
    s += '\n'
print(s)
