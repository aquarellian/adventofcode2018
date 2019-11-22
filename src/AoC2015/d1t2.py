with open("C:/Users/UC247502/IdeaProjects/AoC/adventofcode2018/resources/AoC2015/d1.txt") as f:
    content = f.readlines()

test_str = content[0]
i = 0
sum = 0
while sum >= 0 and i < len(test_str):
    if test_str[i] == "(":
        sum +=1
    elif test_str[i] == ")":
        sum -=1
    i += 1
if sum < 0:
    print(i)
else:
    print('not found')
