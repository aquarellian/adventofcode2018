def phase1(input, pattern):
    pi = 1
    m = 0
    for ch in input:
        i = int(ch)
        m += i * pattern[pi % len(pattern)]
        # print(i, '*', pattern[pi % len(pattern)])
        pi += 1
    # print(m)
    return abs(m) % 10


import load_input
content = load_input.load(2019, 16).split('\n')[0] * 10000
# content='12345678'
# content='80871224585914546619083218645595'
# content='19617804207202209144916044189917'
# content='69317163492948606335995924319873'
content='00000000002948606335995924319873'
output = ''
for ph in range(1, 101):
# for ph in range(1, 5):
    pattern = [0, 1, 0, -1]
    # pattern = [1, 0, -1, 0]
    output = ''
    for i in range(1, len(content)+ 1):
        new_pattern = []
        for v in pattern:
            new_pattern += [v] * i
        # print(new_pattern)
        output += str(phase1(content, new_pattern))
        # print('output', output)
    content = output
    # print(content)
    # print()
print(content)
print(content[10:])

# task2
offset = 10
print(content[offset : offset + 8])