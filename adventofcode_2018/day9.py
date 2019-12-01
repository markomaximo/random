# 477 players; last marble is worth 70851 points

# Two solutions below. The first is mine, and slow for part 2. The second is from reddit, uses deque, which is fast.

from collections import deque
from sys import stdin


def circle_position(start, vector, circle):
    return (start + vector) % len(circle)

def play_round(num_players, scores, circle, current_i, current_marble, end_marble):
    done = False
    for p in range(num_players):
        if current_marble > end_marble:
            done = True
            break

        elif current_marble % 23 == 0:
            to_remove = circle_position(current_i, -7, circle)
            marble_score = current_marble + circle[to_remove]
            scores[p] += marble_score
            del circle[to_remove]
            current_i = circle_position(to_remove, 0, circle)
            current_marble += 1                

        else:
            insert_i = circle_position(current_i, 2, circle)
            circle.insert(insert_i, current_marble)
            current_i = insert_i
            current_marble += 1
    
    return done, scores, circle, current_i, current_marble

num_players = 477
scores = [0] * num_players
circle = [0]
current_i = 0
current_marble = 1
end_marble = 7085100
done = False

while not done:
    done, scores, circle, current_i, current_marble = play_round(num_players,
                                                                 scores, 
                                                                 circle, 
                                                                 current_i, 
                                                                 current_marble, 
                                                                 end_marble)
print(max(scores))


"""
def play_game(num_players, last_marble):
    circle = deque([0])
    scores = [0] * num_players

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % num_players] += circle.pop() + marble
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    return(max(scores))

print(play_game(477, 7085100))
"""