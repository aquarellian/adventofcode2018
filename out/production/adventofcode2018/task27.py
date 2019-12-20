

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

def print_scores(alist, border, count):
    ans = alist[border:border+count]
    strg = ''
    for i, s in enumerate(ans):
        strg += (str(s))
    print(strg)


alist = [3, 7]
elf1 = 0
elf2 = 1
# border=9 #test ok
# border=5 # test ok
# border=18# test ok
# border=2018 # test ok
border=580741


for i in range(0, border + 11):
    # print(i)
    # printout(alist, elf1, elf2)
    alist, elf1, elf2 = make_move(alist, elf1, elf2)
print_scores(alist, border, 10)




