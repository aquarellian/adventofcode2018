class Amplifier:
    index = 0
    content = {}
    out = None
    halted = False
    base = 0

    def __init__(self, content, phase=None):
        self.index = 0
        self.base = 0
        self.content = {k: v for k, v in enumerate(content)}
        if phase is not None:
            self.apply(phase)


    def apply(self, signal):
        return_value = None
        signal_read = False
        while True:
            operator = self.content[self.index]
            oper, mode1, mode2, mode3 = self.parse_oper(operator)
            # print(mode3, mode2, mode1,0, oper)
            if oper != 99:
                p1 = int(self.content[self.index + 1])
                # print(self.content)
            if oper in [1, 2, 5, 6,7,8]:
                p2 = int(self.content[self.index + 2])
                # print(self.content)
            if oper in [1,2,7,8]:
                p3 = int(self.content[self.index + 3])
                # print(self.content)
            if mode3 == 1:
                print('error: value mode for register 3')

            if oper == 1:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                ind = self.get_ind(mode3, p3)
                self.content[ind] = v1 + v2
                self.index += 4
                # print(self.content)
            elif oper == 2:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                ind = self.get_ind(mode3, p3)
                self.content[ind] = v1 * v2
                self.index += 4
                # print(self.content)
            elif oper == 3:
                if not signal_read:
                    # print(mode1)
                    # v1 = self.get_val(mode1, p1)
                    # print(mode1, p1, self.base, v1)
                    # print(self.content.get(int(self.content[p1]) + self.base, 0))
                    ind = self.get_ind(mode1, p1)
                    self.content[ind] = signal
                    self.index += 2
                    signal_read = True
                    # print(self.content)
                else:
                    print('no signal')
                    break
            elif oper == 4:
                v1 = self.get_val(mode1, p1)
                self.index += 2
                # if return_value is not None:
                #     print('error: returning more than one res', return_value, v1)
                return_value = v1
                self.out = v1
                # print('output')
                print(v1)
                # return v1
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
                ind = self.get_ind(mode3, p3)
                self.content[ind] = 1 if v1 < v2 else 0
                self.index += 4
                # print(self.content)
            elif oper == 8:
                v1 = self.get_val(mode1, p1)
                v2 = self.get_val(mode2, p2)
                ind = self.get_ind(mode3, p3)
                self.content[ind] = 1 if v1 == v2 else 0
                self.index += 4
                # print(self.content)
            elif oper == 9:
                v1 = self.get_val(mode1, p1)
                self.base += v1
                self.index += 2
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

    def get_ind(self, mode, val):
        if mode == 0:
            return int(val)
        elif mode == 2:
            return int(val) + self.base
        else:
            print('invalid index mode:', val)

    def get_val(self, mode, val):
        if mode == 1:
            return int(val)
        elif mode in [0, 2]:
            ind = self.get_ind(mode, val)
            if ind < 0:
                print('error: negative index')
            else:
                return int(self.content.get(ind, 0))
        else:
            print('invalid parameter mode')

# 20270370 too low
# 18938402
# 14737954,
# 12640802,
# 19477026,