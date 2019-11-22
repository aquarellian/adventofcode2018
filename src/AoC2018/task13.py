def get_duration(task):
    import string
    return string.ascii_uppercase.index(task) + 1 + 60

with open("../resources/task13.txt") as f:
    content = f.readlines()
    tree = {}
    reversed_tree = {}
    maybe_roots = set()
    not_roots = set()
    for line in content:
        strs = line.split(' ')
        stepBefore = strs[1]
        stepAfter = strs[7]
        if tree.get(stepBefore, None) is None:
            tree[stepBefore] = []
        if reversed_tree.get(stepAfter, None) is None:
            reversed_tree[stepAfter] = []
        tree[stepBefore].append(stepAfter)
        reversed_tree[stepAfter].append(stepBefore)

        not_roots.add(stepAfter)

        if stepAfter in maybe_roots:
            maybe_roots.remove(stepAfter)
        if stepBefore not in not_roots:
            maybe_roots.add(stepBefore)
    aslist = list(maybe_roots)
    aslist.sort()
    root = aslist[0]
    import copy
    next_steps = copy.copy(maybe_roots)
    path = ''

    #task 13
    while len(next_steps) != 0:
        aslist = list(next_steps)
        aslist.sort()
        symbol = aslist[0]

        path += symbol
        next_steps.remove(symbol)
        if tree.get(symbol) is not None:
            for s in tree[symbol]:
                if s not in path and (reversed_tree.get(s, None) is None or all((x in path) for x in reversed_tree[s] )) :
                    next_steps.add(s)
    print(path)

    #task 14
    elves_to_starttime = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    tasks_to_starttime = {}
    for task in maybe_roots:
        tasks_to_starttime[task] = 0

    tasks = list(maybe_roots) + list(not_roots)
    print(tasks)

    print(tree)

    duration = 0
    av_tasks = []
    av_elves = []
    elf_to_task = {}
    path = ''
    done_path = ''
    unlocked = list(maybe_roots)

    while len(tasks) != 0:
        for task, time in tasks_to_starttime.items():
            if time == duration and task in unlocked:
                av_tasks += task

        for elf, time in elves_to_starttime.items():
            if time == duration:
                av_elves.append(elf)
                if elf in elf_to_task:
                    done_path += elf_to_task[elf]

        # print(av_tasks)
        # print(av_elves)

        while len(av_tasks) > 0 and len(av_elves) > 0:
            av_tasks.sort()
            av_elves.sort()
            my_task = av_tasks[0]
            my_elf = av_elves[0]
            elf_to_task[my_elf] = my_task
            print('elf ' + str(my_elf) + ' takes ' + str(my_task) + ' on min ' + str(duration))

            curr_task_duration = get_duration(my_task)
            av_elves.remove(my_elf)
            av_tasks.remove(my_task)
            tasks.remove(my_task)

            elves_to_starttime[my_elf] = duration + curr_task_duration
            path += my_task

            if tree.get(my_task) is not None:
                for s in tree[my_task]:
                    if tasks_to_starttime.get(s, None) is None:
                        tasks_to_starttime[s] = duration + curr_task_duration
                    else:
                        tasks_to_starttime[s] = max(tasks_to_starttime[s], duration + curr_task_duration)
                    if s not in path and (reversed_tree.get(s, None) is None or all((x in path) for x in reversed_tree[s])):
                        unlocked.append(s)

            # print(elves_to_starttime)
            # print(tasks_to_starttime)
            # print(av_tasks)
            # print(av_elves)
            # print(duration)
        duration += 1
        # print(duration)
    print(elves_to_starttime)
    print(tasks_to_starttime)
    print(done_path)
    print(len(done_path) + 1)
    print(max(elves_to_starttime.values()))








