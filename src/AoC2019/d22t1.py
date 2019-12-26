class Node:
    value = None
    next = None
    prev = None

    def __init__(self, value):
        self.value = value

    def append(self, n):
        self.next = n
        n.prev = self
        return n

head = Node(0)
coursor = head
for i in range(1, 10007):
    coursor = coursor.append(Node(i))

def cut(head, tail, n):
    if n > 0:
        cursor = head
        ind = 0
        while ind < n:
            cursor = cursor.next
            ind += 1
        newhead = cursor.next
        newhead.prev = None
        cursor.next = None
        tail.next = head
        head.prev = tail
        return newhead, cursor
    else:
        cursor = tail
        ind = 0
        while ind > n:
            cursor = cursor.prev
            ind -= 1
        newtail = cursor.prev
        newtail.next = None
        cursor.prev = None
        head.prev = tail
        tail.next= head
        return cursor, newtail


def deal(head, tail, n):
    arr = {}
    coursor = head
    index = 0
    while coursor != tail:
        # if index // n < 10007:
        #     index += n
        # # rem += coursor
        # coursor = coursor.next
        # index +=1

        # rem = index % n
        # full = index // n
        # if rem == 0:
        #     arr[index] = coursor
        # else:
        #     arr[full*n - rem] = coursor
        # coursor = coursor.next
        # index +=1





import load_input
content = load_input.load(2019, 22).split(',')


