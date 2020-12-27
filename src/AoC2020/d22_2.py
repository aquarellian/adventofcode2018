import copy
import queue

class player:
    deck = None
    cache = None

    def __init__(self, deck):
        self.deck = queue.Queue()
        [self.deck.put(i) for i in deck]
        self.cache = set()

    def cache_deck(self, qstr):
        self.cache.add(qstr)


def game(player1, player2):
    while not (player1.deck.empty() or player2.deck.empty()):
        str1 = " ".join([str(x) for x in player1.deck.queue])
        str2 = " ".join([str(x) for x in player2.deck.queue])
        if str1 in player1.cache and str2 in player2.cache:
            return player1
        player1.cache_deck(str1)
        player2.cache_deck(str2)
        c1 = player1.deck.get()
        c2 = player2.deck.get()
        if c1 > player1.deck.qsize() or c2 > player2.deck.qsize():
            winner = player1 if c1 > c2 else player2
        else:
            subplayer1 = player(list(player1.deck.queue)[:c1])
            subplayer2 = player(list(player2.deck.queue)[:c2])
            subwinner = game(subplayer1, subplayer2)
            winner = player1 if subwinner == subplayer1 else player2

        if winner == player1:
            player1.deck.put(c1)
            player1.deck.put(c2)
        else:
            player2.deck.put(c2)
            player2.deck.put(c1)
    return player1 if player2.deck.empty() else player2

with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d22.txt") as f:
    content = f.read().split("\n\n")
    arr1 = [int(x.strip()) for x in content[0].split("\n")[1:]]
    arr2 = [int(x.strip()) for x in content[1].split("\n")[1:]]
    player1 = player(arr1)
    player2 = player(arr2)
    qwinner = game(player1, player2)
    res = 0
    ind = qwinner.deck.qsize()
    while not qwinner.deck.empty():
        res += qwinner.deck.get() * ind
        ind -=1
    print(res)







