import opcode
import load_input
content = load_input.load(2019, 7).split(',')
# content = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5] # 139629729 98765

permutations = []
for a in range(5,10):
    b_subset = set(range(5, 10)) - set([a])
    for b in b_subset:
        c_subset = b_subset - set([b])
        for c in c_subset:
            d_subset = c_subset - set([c])
            for d in d_subset:
                e_subset = d_subset - set([d])
                for e in e_subset:
                    permutations.append(str(a) + str(b) + str(c) + str(d) + str(e))


print(permutations)
maxsign = 0
for p in permutations:
    a = opcode.Amplifier(content, int(p[0]))
    b = opcode.Amplifier(content, int(p[1]))
    c = opcode.Amplifier(content, int(p[2]))
    d = opcode.Amplifier(content, int(p[3]))
    e = opcode.Amplifier(content, int(p[4]))

    amps = [a,b,c,d,e]
    signal = 0
    lastsignal = 0
    idx = 0
    halted = False
    # print(p)
    while not halted:
        i = idx % 5
        amp = amps[i]
        signal = amp.apply(signal)
        # print(signal)
        # print(amp.content)
        if amp.halted:
            halted = True
            lastsignal = e.out
        # print(idx, i, signal, amp.halted, amp.out)
        idx+=1
    print(p, lastsignal)
    if lastsignal > maxsign:
        maxsign = lastsignal
print(maxsign)

# too high 139629729
