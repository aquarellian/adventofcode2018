
def nice(s):
    s = s.lower()
    import re
    exclude = ['ab', 'cd', 'pq', 'xy']
    if not re.match(".*[aeiou].*[aeiou].*[aeiou].*", s):
        return False
    if any(x in s for x in exclude):
        return False
    return re.search(re.compile(r"(.)\1"), s) is not None


def nice2(s):
    s = s.lower()

    import re
    import string
    letters = string.ascii_lowercase
    if not any(re.match(".*" + x + "." + x + ".*",  s) for x in letters):
        return False
    return any(re.match(".*" + x + y + ".*" + x + y + ".*",  s) for x in letters for y in letters)

import load_input
content = load_input.load(2015, 5)

count = 0
for s in content.split('\n'):
    if nice(s): # task 1
    # if nice2(s): # task 2
        count += 1
print(count)

# print(nice('ugknbfddgicrmopn'))
# print(nice('aaa'))
# print(not nice('jchzalrnumimnmhp'))
# print(not nice('haegwjzuvuyypxyu'))
# print(not nice('dvszwmarrgswjxmb'))
# print(nice2('qjhvhtzxzqqjkmpb'))
# print(nice2('xxyxx'))
# print(not nice2('uurcxstgmygtbstg'))
# print(not nice2('ieodomkazucvgmuy'))