def count_vals(ch, zeros, ones, twos):
    if ch == '1':
        ones += 1
    elif ch == '2':
        twos += 1
    elif ch == '0':
        zeros += 1
    return zeros, ones, twos

import load_input
content = load_input.load(2019, 8)
layers = {}
w = 25
h = 6

# content = '123456789012' + 'f'
# w = 3
# h = 2


previdx = 0
zeros = 0
ones = 0
twos = 0
min0idx = None

for i, ch in enumerate(content):
    idx = i // (w * h)
    if idx == previdx:
        zeros, ones, twos = count_vals(ch, zeros, ones, twos)
    else:
        layers[previdx] = [zeros, ones, twos]
        if min0idx is None or layers[min0idx][0] > zeros:
            print(min0idx, layers[min0idx][0] if min0idx is not None else 'None', '>', zeros)
            min0idx = previdx
        previdx = idx
        zeros = 0
        ones = 0
        twos = 0
        if ch != 'f':
            zeros, ones, twos = count_vals(ch, zeros, ones, twos)
        else:
            print('processed')
print(layers)
print(layers[min0idx][1] * layers[min0idx][2])
print(layers[min0idx][0])
print(layers[min0idx][1])
print(layers[min0idx][2])
# 2544 low
