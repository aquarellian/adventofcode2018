# import opcode
# opdict = {
#     1: opcode.add
#     2: opcode.mult
# }

import load_input
content = load_input.load(2019, 2).split(',')
# content = content[:-1]

print(content)
# content = [1,9,10,3,2,3,11,0,99,30,40,50]
# content = [1,0,0,0,99]
# content = [2,3,0,3,99]
# content = [2,4,4,5,99,0]
# content = [1,1,1,4,99,5,6,0,99]
ind = 0
content[1] = 12
content[2] = 2
while ind != 99:
    print(ind)
    oper = int(content[ind])
    if oper == 1:
        ind1 = int(content[ind+1])
        ind2 = int(content[ind+2])
        ind3 = int(content[ind+3])
        content[ind3] = int(content[ind1]) + int(content[ind2])
    elif oper == 2:
        ind1 = int(content[ind+1])
        ind2 = int(content[ind+2])
        ind3 = int(content[ind+3])
        content[ind3] = int(content[ind1]) * int(content[ind2])
    elif oper == 99:
        print('halt')
        break
    ind += 4
print(content[0], content)
# 29891 low
