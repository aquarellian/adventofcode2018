import load_input

content = load_input.load(2019, 24).split('\n')[:-1]

# content = ['....#', '#..#.', '#..##', '..#..', '#....']

def is_repeated(contents, content):
    check_contents = set(range(0, len(contents)))
    for row in range(len(content)):
        for i in list(check_contents):
            c = contents[i]
            if c[row] != content[row]:
                check_contents.remove(i)
    return len(check_contents) > 0


def is_bugged(row, column, content):
    return content is not None and 0 <= row < len(content) and 0 <= column < len(content[row]) and content[row][column] == '#'


def print_field(content):
    print(content)
    for line in content:
        print(line)

def biodiv(content):
    mask = ''
    for line in content:
        for ch in line:
            if ch == '#':
                mask = '1' +  mask
            else:
                mask = '0' + mask
    print(mask)
    return int(mask, 2)


def print_layers(layers):
    res = ['','','','','']
    for l in layers:
        res[0] += l[0] + '  '
        res[1] += l[1] + '  '
        res[2] += l[2] + '  '
        res[3] += l[3] + '  '
        res[4] += l[4] + '  '
    print(res[0])
    print(res[1])
    print(res[2])
    print(res[3])
    print(res[4])



def get_update(row, column, level, contents):
    if (row == 2 and column == 2):
        return '.'
    upcontent = contents[level - 1] if level > 0 else None
    downcontent = contents[level + 1] if level < len(contents) -1 else None

    adjacent = is_bugged(row + 1, column, content) + \
               is_bugged(row - 1, column, content) + \
               is_bugged(row, column + 1, content) + \
               is_bugged(row, column - 1, content)
    if row == 0 and upcontent is not None:
        adjacent += is_bugged(1, 2, upcontent)
    if column == 0 and upcontent is not None:
        adjacent += is_bugged(2, 1, upcontent)
    if row == len(content) - 1 and upcontent is not None:
        adjacent += is_bugged(3, 2, upcontent)
    if column == len(content) - 1 and upcontent is not None:
        adjacent += is_bugged(2, 3, upcontent)
    if row == 2 and column == 1:
        for i in range(0, 5):
            adjacent += is_bugged(i, 0, downcontent)
    if row == 2 and column == 3:
        for i in range(0, 5):
            adjacent += is_bugged(i, 4, downcontent)
    if row == 1 and column == 2:
        for i in range(0, 5):
            adjacent += is_bugged(0, i, downcontent)
    if row == 3 and column == 2:
        for i in range(0, 5):
            adjacent += is_bugged(4, i, downcontent)

    if is_bugged(row, column, content) and adjacent != 1:
        # print(row, column, is_bugged(row, column, content), adjacent, '.')
        return '.'
    elif not is_bugged(row, column, content) and 0 < adjacent < 3:
        # print(row, column, is_bugged(row, column, content), adjacent, '#')
        return '#'
    else:
        # print(row, column, is_bugged(row, column, content), adjacent, content[row][column])
        return content[row][column]

# contents = []
# duplicated = False
# ind = 0
# print_field(content)
# while not duplicated:
#     new_content = []
#     for row in range(len(content)):
#         new_line = ''
#         for col in range(len(content[row])):
#             new_line += get_update(row, col, content)
#         new_content.append(new_line)
#     duplicated = is_repeated(contents, new_content)
#     contents.append(new_content)
#     ind += 1
#     print(ind)
#     print_field(new_content)
#     content = new_content
# print(biodiv(content))

layers = []
layers.append(content)
time = 200
# time = 10
while time > 0:
    time -= 1
    new_layer = ['.....', '.....', '.....', '.....', '.....']
    layers.append(new_layer)
    layers.insert(0, list(new_layer))

    new_layers = []
    for i in range(len(layers)):
        content = layers[i]
        new_content = []
        for row in range(len(content)):
            new_line = ''
            for col in range(len(content[row])):
                new_line += get_update(row, col, i, layers)
            new_content.append(new_line)
        new_layers.append(new_content)
    layers = new_layers
    print_layers(layers)
cnt = 0
for l in layers:
    for line in l:
        cnt += line.count('#')
print(cnt)
#2017 too high







