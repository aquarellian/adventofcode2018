# class node:
#     v = None
#     next = None
#
#     def __init__(self, v):
#         self.v=v
#
#     def print(self):
#         cursor = self
#         s = ''
#         while cursor.next != self:
#             s = s + ' ' + str(cursor.v)
#             cursor = cursor.next
#         s = s + ' ' + str(cursor.v)
#         print(s)

def print_arr(arr):
    ind = 1
    s = ''
    while True:
        s += str(arr[ind])
        ind = arr[ind]
        if ind == 1:
            break
    print(s)



def calc_dest(current, excluded):
    dest = current
    while dest == current or dest in excluded:
        dest = dest - 1
        if dest == 0:
            # dest = 9
            dest = 1000000
    return dest

# content = '389125467'#test
# current = 3
content = '792845136'
current = 7
cups = [x+1 for x in range(1000001)]

for i in range(1, 9):
    ind = int(content[i-1])
    cups[ind] = int(content[i])
# cups[int(content[-1])] = int(content[0]) # task 1
cups[int(content[-1])] = 10
cups[1000000] = current
move = 0
size = 9
while move < 10000000:
    move += 1
    dest = calc_dest(current, [cups[current], cups[cups[current]], cups[cups[cups[current]]]])
    old_next = cups[current]
    old_next_next_next = cups[cups[cups[current]]]
    old_after_dest = cups[dest]
    cups[current] = cups[cups[cups[cups[current]]]]
    cups[dest] = old_next
    cups[old_next_next_next] = old_after_dest
    current = cups[current]
    # print_arr(cups)
print(cups[1], cups[cups[1]], cups[1] * cups[cups[1]])
# print_arr(cups)


