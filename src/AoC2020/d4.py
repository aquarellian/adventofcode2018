import re
class passport:
    byr = ''
    iyr = ''
    eyr = ''
    hgt = ''
    hcl = ''
    ecl = ''
    pid = ''
    cid = ''

    year = "^[0-9]{4}$"
    passp = "^[0-9]{9}$"
    height = "^[0-9]{2}in|[0-9]{3}cm$"
    color = "^#[0-9,a-z,A-Z]{6}$"

    def valid(self):
        return re.match(self.year, self.byr) is not None and 1920 <= int(self.byr) <= 2002 and \
               re.match(self.year, self.iyr) is not None and 2010 <= int(self.iyr) <= 2020 and \
               re.match(self.year, self.eyr) is not None  and 2020 <= int(self.eyr) <= 2030 and \
               self.validate_height() and \
               re.match(self.color, self.hcl) is not None  and \
               self.ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and \
               re.match(self.passp, self.pid) is not None

    def validate_height(self):
        return re.match(self.height, self.hgt) is not None  and ( \
                self.hgt.endswith('cm') and 150 <= int(self.hgt[:-2])<=193 or
                self.hgt.endswith('in') and 59 <= int(self.hgt[:-2])<=76)

    def is_santa(self):
        return self.valid() and self.cid == ''

    def set_prop(self, key, value):
        if key.strip() == 'byr':
            self.byr = value.strip()
        elif key.strip() == 'iyr':
            self.iyr = value.strip()
        elif key.strip() == 'eyr':
            self.eyr = value.strip()
        elif key.strip() == 'hgt':
            self.hgt = value.strip()
        elif key.strip() == 'hcl':
            self.hcl = value.strip()
        elif key.strip() == 'ecl':
            self.ecl = value.strip()
        elif key.strip() == 'pid':
            self.pid = value.strip()
        elif key.strip() == 'cid':
            self.cid = value.strip()
        else:
            print('Unknown property:', key, value)

    def print(self):
        print(self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid, self.cid,  self.is_santa(), self.valid())


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d4.txt") as f:
    content = f.read().split('\n\n')
    valid_pass = 0
    for entry in content:
        psprt = passport()
        for prop in entry.replace("\n", " ").split(" "):
            p = prop.split(":")
            psprt.set_prop(p[0], p[1])
        if psprt.valid():
            valid_pass += 1
        psprt.print()
    print(valid_pass)




