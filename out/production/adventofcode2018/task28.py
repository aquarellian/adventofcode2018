table = '37'
elf1 = 0
elf2 = 1
pattern = '580741'

# all ok
# pattern = '51589'
# pattern = '01245'
# pattern = '92510'
# pattern = '59414'

res = {}
mov = {}
rln = {}
for i in range(0, 10):
    mov[str(i)] = 1 + i
    for j in range(0, 10):
        sval = str(i+j)
        res[str(i) + str(j)] = sval
        rln[sval] = len(sval)


i = 0
ln = len(table)
while True:
    elf1v = table[elf1]
    elf2v = table[elf2]
    recipe = res[elf1v + elf2v]
    table += recipe
    ln += rln[recipe]
    elf1 = (elf1 + mov[elf1v]) % ln
    elf2 = (elf2 + mov[elf2v]) % ln
    i += 1
    if i % 100000 == 0:
        print(i)
        if pattern in table:
            break
print(table.index(pattern))
