import load_input
# content = load_input.load(2015, 8)
# content=["\"\"", "\"abc\"", "\"aaa\\\"aaa\"", "\"\\x27\"" ]
content=["\"abc\\x16\\x16\\x16\\x19\\x16\""]
import re
def is_digit(s):
    # return re.compile(r'[0-7][0-7]$').match(s)
    return re.compile(r'\d\d$').match(s)

sum = 0
for line in content:#".split("\n"):
    if len(line) > 0:
        # print(line)
        fulllength = len(line)
        _from = 0
        while "\\x" in line[_from:] and _from < len(line) - 4:
            _from += line[_from:].index('\\x')
            if _from + 4 < len(line) and is_digit(line[_from+2: _from+4]):
                line = line[0:_from] + 'p' + line[_from + 4 :]
            else:
                _from += 1
        line = line.replace('\\\"', '\"').replace('\\\\', '\\')
        fixlength = len(line) - 2
        print(line[1:-1])
        print(fulllength)
        print(fixlength)
        diff = fulllength - fixlength
        sum += diff
print(sum)
# 1341 too high
# 961 wrong
# 1102 wrong
# 1057 wrong
# 1066 wrong
#1111
