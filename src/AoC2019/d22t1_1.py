

def cut(arr, n):
    if n != 0:
        return arr[n:] + arr[:n]
    else:
        return arr


def deal(arr, n = None):
    # print(arr, n)
    if n is None:
        return [ele for ele in reversed(arr)]
        # return arr.reverse()
    newarr = [ele for ele in range(len(arr))]
    for i in range(0, len(arr)):
        mul = i * n
        ind = mul - len(arr) * (mul // len(arr))
        # print(i, '->', ind)
        newarr[ind] = arr[i]
    return newarr

import load_input
content = load_input.load(2019, 22).split('\n')
# content ='deal into new stack\ncut -2\n\ndeal with increment 7\ncut 8\ncut -4\ndeal with increment 7\ncut 3\ndeal with increment 9\ndeal with increment 3\ncut -1\n'.split('\n')
# content = 'deal with increment 7\ndeal into new stack\ndeal into new stack\n'.split('\n')
# content = 'cut 6\ndeal with increment 7\ndeal into new stack\n'.split('\n')
# content = 'deal with increment 7\ndeal with increment 9\ncut -2\n'.split('\n')
content = 'deal with increment 3\ndeal into new stack\ndeal with increment 4\ndeal into new stack'.split('\n')
content = 'deal with increment 3\ndeal with increment \n'.split('\n')
# arr = [ele for ele in range(10007)]
arr = [ele for ele in range(0, 10)]
i = 0
for cmd in content:
    print(i, cmd)
    i+=1
    if 'deal' in cmd:
        if 'increment' in cmd:
            ln = len('deal with increment ')
            num = int(cmd[ln:])
            arr = deal(arr, num)
        elif 'stack' in cmd:
            arr = deal(arr)
        else:
            print('unknown command:', cmd)
    elif 'cut' in cmd:
        ln = len('cut ')
        num = int(cmd[ln:])
        arr = cut(arr, num)
print(arr)
# print(arr[2019])
# 5594 too high
# for i, a in enumerate(arr):
#     if a == 2019:
#         print(i)
#         break


