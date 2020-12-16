def calc_prev_turn(head, prev):
    cursor = head
    if cursor is None:
        return None
    if cursor.val == prev:
        return cursor.turn
    else:
        return calc_prev_turn(cursor.prev, prev)


class node:
    val = None
    turn = None
    prev = None

    def __init__(self, val, turn, prev):
        self.val = val
        self.turn = turn
        self.prev = prev


turn = 1
head = node(9, turn, None)
values = [12, 1, 4, 17, 0, 18]

# example
# head = node(0, turn, None)
# values = [3, 6]
cache = dict()
for v in values:
    print(head.val)
    cache[head.val] = turn
    turn += 1
    head = node(v, turn, head)
prev = values[-1]
# while turn < 2020: # task 1
while turn < 30000000: # task 2
    # print(head.val)
    # print(len(cache))
    turn += 1
    # prev = head.val
    if prev in cache.keys():
        v = cache[prev]
        cache[prev] = turn - 1
        prev = turn - v - 1
        # head = node(turn - v - 1, turn, head)
    else:
        cache[prev] = turn - 1
        prev = 0
    if turn % 1000000 == 0:
        print(turn)
    # print(prev)
        # head = node(0, turn, head)
print(prev)
# print(head.val)

# 175594 high