class Amplifier:
    index = 0
    phase = 0
    content = []
    out = None
    halted = False

    def __init__(self, phase, content):
        self.phase = phase
        self.index = 0
        self.content = list(content)
        self.apply(phase)


    def apply(self, signal):
        return_value = None
        signal_read = False
        while True:
            operator = self.content[self.index]
            oper, mode1, mode2, mode3 = self.parse_oper(operator)
            if oper != 99:
                p1 = int(self.content[self.index + 1])
                # print(self.content)
            if oper in [1, 2, 5, 6,7,8]:
                p2 = int(self.content[self.index + 2])
                # print(self.content)
            if oper in [1,2,7,8]:
                p3 = int(self.content[self.index + 3])
                # print(self.content)
            if mode3 != 0:
                print('error: value mode for register 3')

            if oper == 1:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                self.content[p3] = v1 + v2
                self.index += 4
                # print(self.content)
            elif oper == 2:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                self.content[p3] = v1 * v2
                self.index += 4
                # print(self.content)
            elif oper == 3:
                if not signal_read:
                    self.content[p1] = signal
                    self.index += 2
                    signal_read = True
                    # print(self.content)
                else:
                    break
            elif oper == 4:
                v1 = self.get_val(mode1, p1)
                self.index += 2
                # if return_value is not None:
                #     print('error: returning more than one res', return_value, v1)
                return_value = v1
                self.out = v1
                return v1
                # print(self.content)
            elif oper == 5:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                if v1 != 0:
                    self.index = v2
                else:
                    self.index +=3
                # print(self.content)
            elif oper == 6:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                if v1 == 0:
                    self.index = v2
                else:
                    self.index +=3
                # print(self.content)
            elif oper == 7:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                self.content[p3] = 1 if v1 < v2 else 0
                self.index += 4
                # print(self.content)
            elif oper == 8:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                self.content[p3] = 1 if v1 == v2 else 0
                self.index += 4
                # print(self.content)
            elif oper == 99:
                print('program halted')
                # print(self.content)
                self.halted = True
                break
            else:
                print('program error: invalid operation', oper)
                break
        # return return_value


    def parse_oper(self, oper):
        while len(str(oper)) < 5:
            oper = '0' + str(oper)
        # print(oper)
        oper = int(oper)
        o = oper % 100
        a = oper // 10000
        b = oper % 10000 // 1000
        c = oper % 1000 // 100
        # print(o, c, b, a)
        return o, c, b, a


    def get_val(self, mode, val):
        if mode == 0:
            return int(self.content[int(val)])
        elif mode == 1:
            return int(val)
        else:
            print('invalid parameter mode')

# 20270370 too low
# 18938402
# 14737954,
# 12640802,
# 19477026,