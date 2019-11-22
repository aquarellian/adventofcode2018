with open("C:/Users/UC247502/IdeaProjects/AoC/adventofcode2018/resources/AoC2015/d1.txt") as f:
    content = f.readlines()

test_str = content[0]
print(test_str.count('(') - test_str.count(')'))