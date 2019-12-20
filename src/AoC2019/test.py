count = 7
reaction_outcome = 2
# ('need', 7, 'by', 3, 'reactions producing', 2, 'each, leftover=', -1)
import math

reactions_count = 1 if reaction_outcome > count else int(math.ceil(count / reaction_outcome))
print(count / reaction_outcome)
print(math.ceil(count / reaction_outcome))
print(int(math.ceil(count / reaction_outcome)))
print(reactions_count)
print(reactions_count * reaction_outcome - count)