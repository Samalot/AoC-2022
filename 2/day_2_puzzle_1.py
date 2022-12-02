import Reader


indices = { 'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2 }
win_scores = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

def run():
    total_score = 0
    for round in Reader.read("input"):
        opponent, me = round.split(" ")
        opponent_index, me_index = indices[opponent], indices[me]

        total_score += 1 + me_index + win_scores[opponent_index][me_index]

    return total_score

print(f'Answer: {run()}')
