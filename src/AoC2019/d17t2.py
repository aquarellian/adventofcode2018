def encode(line):
    num = ''
    for ch in line:
        num += str(ord(ch)) + '44'
    num += '10'
    return

def printout(out):
    if out is None:
        return
    line = ''
    for i in out:
        line += chr(i)
    print(line)

def apply_cmd(amp, cmd):
    line = ''
    orig = []
    for i in range(len(cmd)):
        m = cmd[i]
        orig.append(m)
        out = amp.apply(m)
        line += chr(m)
        if i != (len(cmd) - 1):
            out = amp.apply(44)
            line += chr(44)
            orig.append(44)
    out = amp.apply(10)
    line += chr(10)
    orig.append(10)
    print(line)
    print(orig)
    printout(out)

def apply_cmd_bare(amp, cmd):
    for m in cmd:
        out = amp.apply(m)
    printout(out)




import load_input
import opcode

# main = 'ABAABCBCCB'
# main = [ord(ch) for ch in 'ABAABCBCCB']
main = [65, 44, 66, 44, 65, 44, 65, 44, 66, 44, 67, 44, 66, 44, 67, 44, 67, 44, 66, 10]
# a = 'L12R8L6R8L6'
a = [ord('L'), 44, ord('1'), ord('2'), 44, ord('R'), 44, ord('8'), 44, ord('L'), 44, ord('6'), 44, ord('R'), 44, ord('8'), 44, ord('L'), 44, ord('6'), 10]
# b = 'R8L12L12R8'
b = [ord('R'), 44, ord('8'), 44, ord('L'), 44, ord('1'), ord('2'), 44, ord('L'),  44, ord('1'), ord('2'), 44,  ord('R'), 44, ord('8'), 10]
# c = 'L6R6L12'
c = [ord('L'), 44,  ord('6'), 44, ord('R'), 44,  ord('6'), 44, ord('L'), 44,  ord('1'), ord('2'), 10]
print(a, b, c)
content = load_input.load(2019, 17).split(',')
content[0] = 2
amp = opcode.Amplifier(content)
out = amp.apply(None)
printout(out)
apply_cmd_bare(amp, main)
apply_cmd_bare(amp, a)
apply_cmd_bare(amp, b)
apply_cmd_bare(amp, c)
out = amp.apply(ord('n'))
out = amp.apply(10)
print(out)

# print(main)
# print(a)
# for i in a:
#     out = amp.apply(i)
# printout(out)

# print(b)
# for i in b:
#     out = amp.apply(i)
# printout(out)
# for i in c:
#     out = amp.apply(i)
# printout(out)
# out = amp.apply(ord('y'))
# printout(out)



# while not amp.halted:
#
#     v = amp.apply(None)
#
#     if v == 35:
#         line += '#'
#     elif v == 46:
#         line += '.'
#     elif v == 10:
#         _map[ind] = line
#         line = ''
#         ind += 1
#     elif v is not None:
#         line += str(chr(v))
#         print('unknown symbol', v, chr(v))

# res = 0
# for i in range(max(_map.keys()) + 1):
#     line = _map[i]
#     print(line)
#     for j in range(len(line)):
#         if line[j] == '#' and 0 < j < len(line) - 1 and 0 < i < max(_map.keys()) and line[j-1] == '#' and line[j+1] == '#' and  _map[i-1][j] == '#' and _map[i+1][j]== '#':
#             res += i*j
# print(res)
#
# content = load_input.load(2019, 17).split(',')
# content[0] = 2
# amp = opcode.Amplifier(content)
# print(chr(amp.apply(None)))