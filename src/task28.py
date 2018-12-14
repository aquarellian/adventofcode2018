

def get_score(alist, elf1, elf2):
    score = alist[elf1] + alist[elf2]
    return [int(a) for a in str(score)]


def make_move(alist, elf1, elf2):
    new_scores = get_score(alist, elf1, elf2)
    for score in new_scores:
        alist.append(score)
    elf1 = select_current(alist, elf1)
    elf2 = select_current(alist, elf2)
    return alist, elf1, elf2


def select_current(alist, elf):
    return (elf + alist[elf] + 1) % len(alist)


def printout(alist, elf1, elf2):
    strg = ''
    for i, s in enumerate(alist):
        if i == elf1:
            strg += ('(' + str(s) + ') ')
        elif i == elf2:
            strg += ('[' + str(s) + '] ')
        else:
            strg += (str(s) + ' ')
    print(strg)

def as_str(alist):
    strg = ''
    for i, s in enumerate(alist):
        strg += str(s)
    return strg

def print_result(strg, pattern):
    print(strg.index(pattern))


alist = [3, 7]
elf1 = 0
elf2 = 1
# pattern = '51589' # test ok
# pattern = '01245' # test ok
# pattern = '92510' # test ok
# pattern = '59414' # test ok
pattern = '580741'

i = 0
while pattern not in as_str(alist) :
    alist, elf1, elf2 = make_move(alist, elf1, elf2)
    # printout(alist, elf1, elf2)
    i+= 1
# print(as_str(alist))
print_result(as_str(alist), pattern)




