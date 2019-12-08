import opcode
import load_input
content = load_input.load(2019, 7).split(',')

phase = range(0, 5)
permutations = []


for a in range(0,5):
    b_subset = set(range(0,5)) - set([a])
    for b in b_subset:
        c_subset = b_subset - set([b])
        for c in c_subset:
            d_subset = c_subset - set([c])
            for d in d_subset:
                e_subset = d_subset - set([d])
                for e in e_subset:
                    permutations.append(str(a) + str(b) + str(c) + str(d) + str(e))


maxsign = 0
for p in permutations:
    a = opcode.Amplifier(int(p[0]), content)
    b = opcode.Amplifier(int(p[1]), content)
    c = opcode.Amplifier(int(p[2]), content)
    d = opcode.Amplifier(int(p[3]), content)
    e = opcode.Amplifier(int(p[4]), content)

    amps = [a,b,c,d,e]
    signal = a.apply(0)
    print(signal)
    signal = b.apply(signal)
    print(signal)
    signal = c.apply(signal)
    print(signal)
    signal = d.apply(signal)
    print(signal)
    signal = e.apply(signal)
    print(signal, p)
    if signal > maxsign:
        maxsign = signal
print(maxsign)
#17614 low
#56614 if 32410