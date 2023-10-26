# scores = [181, 124, 165, 174]
scores_str = input('Give comma-separated list of scores: ')
scores = [int(s.strip()) for s in scores_str.split(',')]

highest_score = 0

for score in scores:
    if score > highest_score:
        highest_score = score

print(f"Highest score is {highest_score}")