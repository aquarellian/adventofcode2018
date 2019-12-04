def get_mass(v):
    mass = (v / 3) - 2
    if mass > 0:
        return mass + get_mass(mass)
    else:
        return 0



import load_input
content = load_input.load(2019, 1)
sum = 0
# content='1969'
for line in content.split('\n'):
    if line != '':
        # num = (int(line) / 3) - 2
        sum += get_mass(int(line))
print(sum)

# 2478911
# 3305301
# 4955106