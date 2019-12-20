# example
# players_cnt = 9
# marbles_cnt = 25

# test 1 ok
# players_cnt = 10
# marbles_cnt = 1618

# # test 2 ok
# players_cnt = 13
# marbles_cnt = 7999

# test 3 ok
# players_cnt = 17
# marbles_cnt = 1104

# test 4 ok
# players_cnt = 21
# marbles_cnt = 6111

# test 5 ok
# players_cnt = 30
# marbles_cnt = 5807

# actual
players_cnt = 424
marbles_cnt = 7114400
class Marble:
    def __init__(self, value, next_v=None, prev_v=None):
        self.value = value
        self.next_v = self if next_v is None else next_v
        self.prev_v = self if prev_v is None else prev_v

    def add_next(self, marble):
        # print('add ' + str(marble.value) + ' after ' + str(self.value))
        prev_next = self.next_v
        self.next_v = marble
        marble.prev_v = self
        marble.next_v = prev_next
        prev_next.prev_v = marble
        # print('added ' + str(marble.value) + ' after ' + str(marble.prev_v.value))


# spare_marbles = set([i for i in range(1, marbles_cnt+1)])
def do_print(marble):
    val = marble.value
    pnt = marble.next_v
    strng = str(val)
    while pnt.value != val:
        strng += (' ' + str(pnt.value))
        pnt = pnt.next_v
    print(strng)


scores = {}
marble_ind = 0
game = Marble(marble_ind)
head = game
scored_player = 0
while marble_ind < marbles_cnt:
    # do_print(head)
    marble_ind += 1
    marble = Marble(marble_ind)
    if marble.value % 23 != 0:
        game.next_v.add_next(marble)
        game = marble
    else:
        # do_print(game)
        back6 = game.prev_v.prev_v.prev_v.prev_v.prev_v.prev_v
        back7 = back6.prev_v
        back8 = back7.prev_v
        game = back6
        back8.next_v = back6
        back6.prev_v = back8
        score = marble.value + back7.value
        scored_player = players_cnt if marble.value % players_cnt == 0 else marble.value % players_cnt
        # print('player ', scored_player, ' scored with ', score, ' with total ', scores.get(scored_player, 0) + score)
        scores[scored_player] = scores.get(scored_player, 0) + score
        # print(scores)
# print(scores)

print(max(scores.values()))

