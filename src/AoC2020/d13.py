# task 1
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d13.txt") as f:
    content = f.readlines()
    val = int(content[0])
    buses = [int(x) for x in content[1].split(',') if x != 'x']
    minwait = val
    mybus = None
    for bus in buses:
        mod = val % bus
        if mod == 0:
            print('bus ' + bus + ' right away')
            break
        wait = bus - mod
        if wait < minwait:
            minwait = wait
            mybus = bus
    print(mybus, minwait, mybus * minwait)

# task2
with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d13_test.txt") as f:
    content = f.readlines()
    buses = dict()
    data = content[1].split(',')
    maxbus = 0
    for i in range(len(data)):
        if data[i] != 'x':
            buses[int(data[i])] = i
            # buses[i] = int(data[i])
            maxbus = max(maxbus, int(data[i]))
    # condition = False
    # # i = 221000000
    # val = 0
    # while not condition:
    #     i += 1
    #     val = maxbus * i - buses[maxbus]
    #     condition = True
    #     for bus, ind in buses.items():
    #         condition &= ((bus - val % bus) % bus == ind % bus)
    #         if not condition:
    #             break
    #     if i % 1000000 == 0:
    #         print(i, val)
    # print(val)
    k = 1
    first = int(data[0])
    for bus, ind in buses.items():
        if ind != 0:
            condition = False
            i = 0
            while not condition:
                i+=1
                val = first * i
                if val % bus == ind % bus:
                    k *= i
                    break
    print(k*first)


    # task 2.1







