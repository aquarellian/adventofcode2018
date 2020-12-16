def can_connect(sorted_array):
    current = sorted_array[0]
    for x in array:
        if x - current > 3:
            return False
    return True


def count_ways(sorted_array, goal, cache):
    if cache.get((frozenset(sorted_array), goal)) is not None:
        return cache.get((frozenset(sorted_array), goal))
    count = 0 if len(sorted_array) > 3 else 1
    if len(sorted_array) > 1 and goal - (sorted_array[-1]) < 4:
        res = count_ways(sorted_array[:-1], sorted_array[-1], cache)
        cache[(frozenset(sorted_array[:-1]), sorted_array[-1])] = res
        count += res
    if len(sorted_array) > 2 and goal - (sorted_array[-2]) < 4:
        res = count_ways(sorted_array[:-2], sorted_array[-2], cache)
        cache[(frozenset(sorted_array[:-2]), sorted_array[-2])] = res
        count += res
    if len(sorted_array) > 3 and goal - (sorted_array[-3]) < 4:
        res = count_ways(sorted_array[:-3], sorted_array[-3], cache)
        cache[(frozenset(sorted_array[:-3]), sorted_array[-3])] = res
        count += res
    return count


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d10.txt") as f:
    content = f.readlines()
    array = sorted([int(x) for x in content])
    current = 0
    jolt1=0
    jolt3=0
    for x in array:
        diff = x - current
        if diff <=3:
            current = x
            if diff == 1:
                jolt1+=1
            elif diff == 3:
                jolt3 +=1
        else:
            print('eh?')
    print(jolt1*(jolt3 + 1))
    goal = array[-1] + 3

    print(count_ways([0] + array, goal, dict()))

# 259172170858496 low
# 518344341716992