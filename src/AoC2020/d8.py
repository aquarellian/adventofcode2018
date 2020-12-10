class command:
    cmd = None
    par = None
    def __init__(self, cmd, par):
        self.cmd = cmd
        self.par = par

    def exec(self, acc, pos):
        if self.cmd == 'nop':
            return acc, pos + 1
        elif self.cmd == 'acc':
            return acc + self.par, pos + 1
        elif self.cmd == 'jmp':
            return acc, pos + self.par

def execute(arr):
    pos = 0
    acc = 0
    arr_exec = [False for x in range(len(content))]
    while True:
        # task 2
        if pos >= len(content):
            print('final res:', acc)
            return True
        # task 1
        if arr_exec[pos]:
            print('cycle!', acc)
            return False
        cmd = arr[pos]
        arr_exec[pos] = True
        (acc, pos) = cmd.exec(acc, pos)



with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d8.txt") as f:
    content = f.readlines()
    arr = [None for x in range(len(content))]

    for i in range(0, len(content)):
        strs = content[i].split(" ")
        cmd = command(strs[0], int(strs[1]))
        arr[i] = cmd

    execute(arr) # task 1

    pos = 0
    acc = 0
    arr_exec = [False for x in range(len(content))]
    exec_arr = list()
    while True:
        if pos >= len(content):
            print('final res:', acc)
            break
        # task 1
        if arr_exec[pos]:
            print('cycle!', acc)
            break
        exec_arr.append(pos)
        cmd = arr[pos]
        arr_exec[pos] = True
        # print(pos, cmd.cmd, cmd.par, ind)
        (acc, pos) = cmd.exec(acc, pos)


    for changing_pos in reversed(range(len(exec_arr))):
        actual_pos = exec_arr[changing_pos]
        new_arr = arr.copy()
        suspect = arr[actual_pos]
        if suspect.cmd == 'jmp':
            suspect.cmd = 'nop'
            # new_arr[actual_pos] = command('nop', suspect.par)
            if execute(new_arr):
                break
        elif suspect.cmd == 'nop':
            suspect.cmd = 'jmp'
            # new_arr[actual_pos] = command('jmp', suspect.par)
            if execute(new_arr):
                break










