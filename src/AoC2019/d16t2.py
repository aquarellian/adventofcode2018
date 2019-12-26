# def phase1(input, pattern, index):
#     # pi = 1
#     m = 0
#     meet1 = False
#     for ch in input: # todo skip 0s
#         v = int(input[i])
#         p = pattern[pi % len(pattern)]
#         # if p == 1:
#         #     meet1 = True
#         # elif meet1:
#         #     i += index # skip 0s in the middle
#         #     pi += index
#         #     continue
#         m += v * p
#         # print(i, '*', pattern[pi % len(pattern)])
#         pi += 1
#     # print(m)
#     return abs(m) % 10

def phase1(input, pattern, index = 1):
    pi = index
    m = 0
    meet1 = False
    for chi in range(index - 1, len(input)):
        p = pattern[pi % len(pattern)]
        if p == 1:
            meet1 = True
        elif meet1:
            chi += index # skip 0s in the middle
            pi += index
            continue
        else:
            pi += 1
            continue
        i = int(input[chi])
        m += i * p
        # print(i, '*', pattern[pi % len(pattern)])
        pi += 1
    # print(m)
    return abs(m) % 10


import load_input
# content = load_input.load(2019, 16).split('\n')[0] * 10000
# offset = int(content[:7])
# content='69317163492948606335995924319873'
# content='12345678'
# offset = 10
# print(len('36380240000032386911569077141342487018647662249433376832833889043036828088043018099950985754914646505842706004341131661223168302107660848684709603973038355899268638524050008238191106902714634298706864266274948337183233383904803632803804801859990098075441469650084220605434613116127316330260761084368420965397803885584926'))
# content='03036732577212944063491565474664' * 10000
content='03036732577212944063491565474664' * 10000
offset = int(content[:7])

cleng = len(content)
content = content[offset:]
# print(content)
print(offset, cleng, len(content))
# content='12345678'
# content = content[offset:]
# content='19617804207202209144916044189917'
# content='69317163492948606335995924319873'
output = ''
for ph in range(1, 101):
# for ph in range(1, 5):
    pattern = [0, 1, 0, -1]
    output = ''
    # for i in range(offset,  offset + 4):
    for i in range(offset, len(content) + offset):
        new_pattern = []
        for v in pattern:
            new_pattern += [v] * (i + 1)
        output += str(phase1(content, new_pattern[offset:], i-offset))
    content = output
    # print(ph, content)
    print(ph, content[:8])

print(content[:8])

