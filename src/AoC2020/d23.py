class node:
    v = None
    next = None

    def __init__(self, v):
        self.v=v

    def print(self):
        cursor = self
        s = ''
        while cursor.next != self:
            s = s + ' ' + str(cursor.v)
            cursor = cursor.next
        s = s + ' ' + str(cursor.v)
        print(s)

def calc_dest(current, excluded):
    dest = current
    while dest == current or dest in excluded:
        dest = dest - 1
        if dest == 0:
            # dest = 9
            dest = 100
    return dest

content = '389125467'#test
head = node(3)
# content = '792845136'
# head = node(7)
cursor = head
for i in range(1, 100):
    if i < len(content):
        cursor.next = node(int(content[i]))
    else:
        cursor.next = node(i+1)
    cursor = cursor.next
cursor.next = head
last = cursor
move = 0
size = 9
while move < 100:
    move += 1
    current = head.v
    dest = calc_dest(head.v, [head.next.v, head.next.next.v, head.next.next.next.v])
    trio = head.next
    head.next = head.next.next.next.next
    head = head.next
    cursor = head
    wrapped = False
    while cursor.v != dest:
        if cursor.v < 10 or wrapped:
            cursor = cursor.next
        else:
            cursor = last
            wrapped = True
    trio.next.next.next = cursor.next
    cursor.next = trio
    head.print()
    print()
    # print()

cursor = head
while cursor.v != 1:
    cursor = cursor.next
print(cursor.next.v)
print(cursor.next.next.v)
print(cursor.next.v * cursor.next.next.v)


