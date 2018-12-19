# example
# players_cnt = 9
# marbles_cnt = 25

# test 1 ok
players_cnt = 10
marbles_cnt = 270

# # test 2 uncertain
# players_cnt = 13
# marbles_cnt = 146373

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
# players_cnt = 424
# marbles_cnt = 71144

spare_marbles = set([i for i in range(1, marbles_cnt+1)])
game = [0]

def make_move(ind):
    if len(spare_marbles) == 0:
        return ind, 0
    score = 0
    marble = min(spare_marbles)
    spare_marbles.remove(marble)
    if marble % 23 == 0:
        score += marble
        extra_ind = ind-7
        while extra_ind < 0:
            extra_ind += len(game)
        extra_marble = game[extra_ind]
        score += extra_marble

        game.remove(extra_marble)
        while extra_ind >= len(game):
            extra_ind -= len(game)
        ind = extra_ind
    else:
        extra_ind = ind+2
        while extra_ind > len(game):
            extra_ind -= len(game)
        if extra_ind == len(game):
            game.append(marble)
        else:
            game.insert(extra_ind, marble)
        ind = extra_ind
    return ind, score


scores = {}
head_ind = 0

scoring_margin = 23 % players_cnt
for i in range(23, marbles_cnt, 23):
    score = 23 + ?
    scores[i] = scores.get(i, 0) + score

print(max(scores.values()))

