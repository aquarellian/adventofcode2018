import load_input
content = load_input.load(2019, 4).split('-')
_from = content[0]
_to = content[1]
print(_from)
print(_to)

import re
def doubleDigit(val):
    pattern = re.compile(r"(.)\1")
    matches = re.findall(pattern, val)
    if matches is None:
        return False
    else:
        for gr in matches:
            print('gr=',gr)
            cnt = 0
            for ch in val:
                print('ch=', ch)
                if cnt == 1 and ch != gr:
                    cnt = 0
                elif ch == gr:
                    cnt+=1
                    # if cnt > 2:
                    #     break
            print(cnt)
            if cnt == 2:
                return True
    return False

def numsInc(val):
    for i in range(0, len(val)-1):
        if int(val[i]) > int(val[i+1]):
            return False
    return True


def next(val):
    if len(val) == 0:
        return ''
    elif val[len(val)-1] != '9':
        return val[:len(val)-1] + str(int(val[len(val)-1]) + 1)
    else:
        tmp = next(val[:len(val)-1])
        return tmp + tmp[len(tmp)-1]

# vals = ['122345', '111123', '135679', '111111', '223450', '123789']
# vals = ['111224']
# for val in vals:
#     print(val, ' ', (doubleDigit(val) and numsInc(val)))

counter = 0
val = _from
while int(val) <= int(_to):
    if doubleDigit(val) and numsInc(val):
        counter += 1
    val = next(val)
    # print(val)

print(counter)




