import Reader


indices = { 'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 1, 'Z': 2 }
my_choice = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]

def run():
    total_score = 0
    for round in Reader.read("input"):
        opponent, me = round.split(" ")
        opponent_index, me_index = indices[opponent], indices[me]

        total_score += my_choice[opponent_index][me_index] + (me_index * 3)

    return total_score


print(f'Answer: {run()}')