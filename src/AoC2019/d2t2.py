
import load_input

def process(noun, verb):
    content = load_input.load(2019, 2).split(',')
    ind = 0
    content[1] = noun
    content[2] = verb
    while ind != 99:
        # print(ind)
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
            # print('halt')
            break
        ind += 4
    return content[0]


for i in range(99, -1, -1):
    for j in range(99, -1, -1):
        v = process(i, j)
        if v ==19690720:
            print( 100 * i + j)
            break
    print(i)
