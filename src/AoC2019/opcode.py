def apply(content, input):
    index = 0
    # print(content)
    with open('test.txt', 'w') as r:
        while True:
            r.write(str(content) + '\n')
            par_num = 1
            operator = content[index]
            oper, mode1, mode2, mode3 = parse_oper(operator)
            if oper != 99:
                p1 = int(content[index + 1])
            if oper in [1, 2, 5, 6,7,8]:
                p2 = int(content[index + 2])
            if oper in [1,2,7,8]:
                p3 = int(content[index + 3])
            if mode3 != 0:
                print('error: value mode for register 3')

            if oper == 1:
                v1 = get_val(content, mode1, p1)
                v2 = get_val(content, mode2, p2)
                content[p3] = v1 + v2
                index += 4
            elif oper == 2:
                v1 = get_val(content, mode1, p1)
                v2 = get_val(content, mode2, p2)
                content[p3] = v1 * v2
                index += 4
            elif oper == 3:
                content[p1] = input
                index += 2
            elif oper == 4:
                v1 = get_val(content, mode1, p1)
                index += 2
                print(v1)
            elif oper == 5:
                v1 = get_val(content, mode1, p1)
                v2 = get_val(content, mode2, p2)
                if v1 != 0:
                    index = v2
                else:
                    index +=3
            elif oper == 6:
                v1 = get_val(content, mode1, p1)
                v2 = get_val(content, mode2, p2)
                if v1 == 0:
                    index = v2
                else:
                    index +=3
            elif oper == 7:
                v1 = get_val(content, mode1, p1)
                v2 = get_val(content, mode2, p2)
                content[p3] = 1 if v1 < v2 else 0
                index += 4
            elif oper == 8:
                v1 = get_val(content, mode1, p1)
                v2 = get_val(content, mode2, p2)
                content[p3] = 1 if v1 == v2 else 0
                index += 4
            elif oper == 99:
                print('program halted')
                print(content)
                break
            else:
                print('program error: invalid operation', oper)
                break


def parse_oper(oper):
    while len(str(oper)) < 5:
        oper = '0' + str(oper)
    # print(oper)
    oper = int(oper)
    o = oper % 100
    a = oper // 10000
    b = oper % 10000 // 1000
    c = oper % 1000 // 100
    # print(o, c, b, a)
    return o, c, b, a


def get_val(content, mode, val):
    if mode == 0:
        return int(content[int(val)])
    elif mode == 1:
        return int(val)
    else:
        print('invalid parameter mode')
